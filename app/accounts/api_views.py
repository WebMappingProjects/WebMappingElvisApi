from rest_framework import status, viewsets
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.decorators import action
from accounts.models import User, StoredRefreshToken
from accounts.serializers import *
from accounts.permissions import *
from rest_framework import filters
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.utils import timezone as tz
from threading import Thread
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import TemplateDoesNotExist, render_to_string
from django.utils.html import strip_tags
from django.utils.timezone import now
from django.core.mail import send_mail
import random
from datetime import timezone, datetime, timedelta

class TemplateEmail(Thread):    
    def __init__(
        self,
        to,
        subject,
        template,
        context,
        from_email=None,
        reply_to=None,
        app_name='accounts',
        *args,
        **email_kwargs,
    ):
        super().__init__(*args, **email_kwargs)
        
        self.to = to
        self.subject = subject
        self.template = template
        self.context = context
        self.from_email = from_email or settings.EMAIL_HOST_USER
        self.reply_to = reply_to
        self.app_name = app_name

        self.html_content, self.plain_content = self.render_content()

        self.to = self.to if not isinstance(self.to, str) else [self.to]

        if self.reply_to:
            self.reply_to = (
                self.reply_to if not isinstance(self.reply_to, str) else [self.reply_to]
            )

        self.django_email = EmailMultiAlternatives(
            subject=self.subject,
            body=self.plain_content,
            from_email=self.from_email,
            to=self.to,
            reply_to=self.reply_to,
            **email_kwargs,
        )
        self.django_email.attach_alternative(self.html_content, "text/html")
        self.django_email.mixed_subtype = "related"

    def render_content(self):
        html_content = self.render_html()

        try:
            plain_content = self.render_plain()
        except TemplateDoesNotExist:
            plain_content = strip_tags(html_content)

        return html_content, plain_content

    def render_plain(self):
        return render_to_string(self.get_plain_template_name(), self.context)

    def render_html(self):
        template_name = self.get_html_template_name()
        return render_to_string(template_name, self.context)

    def get_plain_template_name(self):
        return f"{self.app_name}/email/{self.template}.txt"

    def get_html_template_name(self):
        return f"{self.app_name}/email/{self.template}.html"
    
    def send(self, **send_kwargs):
        return self.django_email.send(**send_kwargs)
    
    def run(self, **run_kwargs):
        self.send(**run_kwargs)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        """Override pour stocker le refresh token émis."""
        response = super().post(request, *args, **kwargs)

        refresh_token = None
        try:
            refresh_token = response.data.get('refresh')
        except Exception:
            refresh_token = None

        user = None
        if request.user and request.user.is_authenticated:
            user = request.user
        else:
            # fallback: try to get user by username/email from response data or request data
            identifier = response.data.get('username') or response.data.get('email') or request.data.get('identifier') or request.data.get('username') or request.data.get('email')
            if identifier:
                user = User.objects.filter(username__iexact=identifier).first() or User.objects.filter(email__iexact=identifier).first()

        if user:
            # Revoke all previous refresh tokens for this user
            StoredRefreshToken.objects.filter(user=user, revoked=False).update(revoked=True)

        # Remove all revoked refresh tokens for this user
        if user:
            # Supprimer tous les tokens dont la date d'expiration est déjà dépassée
            StoredRefreshToken.objects.filter(expires_at__lt=tz.now()).delete()

        if refresh_token:
            try:
                rt = RefreshToken(refresh_token)
                jti = rt.get('jti')
                exp = rt.get('exp')
                expires_at = timezone.datetime.fromtimestamp(exp, tz=timezone.utc) if exp else None
            except Exception:
                jti = None
                expires_at = None

            StoredRefreshToken.objects.create(
                user=(request.user if request.user and request.user.is_authenticated else user),
                refresh_token=refresh_token,
                jti=jti,
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:512],
                expires_at=expires_at,
            )

        # Delete existing cookies if they exist
        if 'refresh_token' in request.COOKIES:
            response.delete_cookie('refresh_token')
        if 'authenticated' in request.COOKIES:
            response.delete_cookie('authenticated')

        # Set new cookies
        response.set_cookie(
            'refresh_token',
            refresh_token,
            httponly=True,
            secure=True,
            samesite='Lax',
            max_age=14 * 24 * 60 * 60,  # 14 jours
            path='/'
        )
        response.set_cookie(
            'authenticated',
            'true',
            httponly=False,
            secure=True,
            samesite='Lax',
            max_age=14 * 24 * 60 * 60  # 14 jours
        )
        # Remove refresh token from response data
        if 'refresh' in response.data:
            del response.data['refresh']

        return response


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ["username", "email", "role"]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            response_data = {
                # 'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }

            # stocke le refresh token
            try:
                jti = refresh.get('jti')
                exp = refresh.get('exp')
                expires_at = timezone.datetime.fromtimestamp(exp, tz=timezone.utc) if exp else None
            except Exception:
                jti = None
                expires_at = None

            StoredRefreshToken.objects.create(
                user=user,
                refresh_token=str(refresh),
                jti=jti,
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:512],
                expires_at=expires_at,
            )

            response = Response(response_data, status=status.HTTP_201_CREATED)
            # Delete existing cookies if they exist
            if 'refresh_token' in request.COOKIES:
                response.delete_cookie('refresh_token')
            if 'authenticated' in request.COOKIES:
                response.delete_cookie('authenticated')

            # Set new cookies
            response.set_cookie(
                'refresh_token',
                str(refresh),
                httponly=True,
                secure=True,
                samesite='Lax',
                max_age=14 * 24 * 60 * 60  # 14 jours
            )
            response.set_cookie(
                'authenticated',
                'true',
                httponly=False,
                secure=True,
                samesite='Lax',
                max_age=14 * 24 * 60 * 60  # 14 jours
            )

            # return Response(response_data, status=status.HTTP_201_CREATED)
            return response
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CanManageUsers]  # Seuls les admins peuvent gérer les utilisateurs
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["username", "email", "role"]
    ordering_fields = ["username", "email", "role"]

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        """Retourne les informations de l'utilisateur connecté"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'], url_path='logout', permission_classes=[permissions.IsAuthenticated])
    def logout_user(self, request):
        # Get refresh token from cookie or request body
        refresh_str = request.COOKIES.get('refresh_token')
        if refresh_str:
            # Find and revoke the stored refresh token
            stored_token = StoredRefreshToken.objects.filter(refresh_token=refresh_str).first()
            if stored_token:
                stored_token.revoked = True
                stored_token.save()

        response = Response({
            "status": status.HTTP_200_OK,
            "message": "success",
        })

        # Delete cookies
        response.delete_cookie('refresh_token')
        response.delete_cookie('authenticated')
        logout(request)
        return response
    
    @action(detail=True, methods=['POST'], url_path='change-role', permission_classes=[IsAdmin])
    def change_role(self, request, pk=None):
        """Permet de changer le rôle d'un utilisateur"""
        user = self.get_object()
        new_role = request.data.get('role')
        
        if new_role not in ['admin', 'decideur', 'technicien', 'lambda']:
            return Response(
                {'error': 'Rôle invalide'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.role = new_role
        user.save()
        
        return Response(
            {'message': f'Rôle changé en {new_role}'}, 
            status=status.HTTP_200_OK
        )

    @action(detail=False, url_path="send-reset-code", methods=['post'], permission_classes=[permissions.AllowAny])
    def generate_code(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email requis"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"error": "Cet email n'est associé à aucun compte"}, status=status.HTTP_404_NOT_FOUND)

        code = str(random.randint(100000, 999999))
        expires_at = now() + timedelta(minutes=15)

        user.code = code
        user.code_expires_at = expires_at
        user.save()

        email_context = {
            'code': code,
            'expires_at': expires_at.strftime('%Y-%m-%d %H:%M:%S'),
            'user': user
        }

        template_email = TemplateEmail(
            to=email,
            subject="Réinitialisation de votre mot de passe",
            template="reset_code",
            context=email_context
        )
        template_email.start()

        return Response({"success": True, "message": "Code envoyé avec succès"})

    @action(detail=False, url_path="verify-code", methods=['post'], permission_classes=[permissions.AllowAny])
    def verify_code(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        if not email or not code:
            return Response({"error": "Tous les champs sont requis"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(
            email=email, code=code, code_expires_at__gt=now()
        ).first()

        if not user:
            return Response({"error": "Code invalide ou expiré"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"success": True, "message": "Le code est valide"})

    @action(detail=False, url_path="reset-password", methods=['post'], permission_classes=[permissions.AllowAny])
    def reset_password(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        new_password = request.data.get('new_password')
        if not email or not code or not new_password:
            return Response({"error": "Tous les champs sont requis"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(
            email=email, code=code
        ).first()

        if not user:
            return Response({"error": "Code invalide"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"error": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        user.set_password(new_password)
        user.code = None
        user.save()

        return Response({"success": True, "message": "Mot de passe réinitialisé avec succès"})
    
    @action(detail=False, url_path="change-password", methods=['patch'], permission_classes=[permissions.IsAuthenticated])
    def change_password(self, request):
        old_password = request.data.get('password')
        new_password = request.data.get('new_password')

        if not old_password or not new_password:
            return Response({"error": "Tous les champs sont requis"}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        if not user.check_password(old_password):
            return Response({"error": "Mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"success": True, "message": "Mot de passe changé avec succès"})

    @action(detail=True, methods=['DELETE'], url_path='delete-account', permission_classes=[permissions.IsAuthenticated])
    def delete_account(self, request, pk=None):
        """Permet à un utilisateur de supprimer son compte"""
        user = self.get_object()
        
        # Vérifier que l'utilisateur supprime son propre compte ou est admin
        if request.user != user and not request.user.is_superuser:
            return Response(
                {'error': 'Vous ne pouvez pas supprimer le compte d\'un autre utilisateur'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Supprimer les refresh tokens
        StoredRefreshToken.objects.filter(user=user).delete()
        
        # Supprimer l'utilisateur
        user.delete()
        
        response = Response(
            {'message': 'Compte supprimé avec succès'}, 
            status=status.HTTP_200_OK
        )
        
        # Supprimer les cookies si l'utilisateur supprime son propre compte
        if request.user == user:
            response.delete_cookie('refresh_token')
            response.delete_cookie('authenticated')
        
        return response

class AdminViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.filter(is_superuser=True)
    serializer_class = AdminSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["username", "email"]
    ordering_fields = ["username", "email"]


# class TokenRefreshView(TokenRefreshView):
#     """
#     API View pour rafraîchir un token JWT.
#     Attend un refresh token dans le corps de la requête et retourne un nouveau access token.
#     """
#     permission_classes = [permissions.AllowAny]


class TokenViewSet(viewsets.ViewSet):
    """ViewSet exposant une action pour rafraichir le token JWT."""
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'], url_path='refresh')
    def refresh(self, request):
        # Retrieve refresh token only from cookies
        refresh_str = request.COOKIES.get('refresh_token')
        if not refresh_str:
            return Response({'detail': 'Refresh token manquant dans les cookies.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate token structure
        try:
            rt = RefreshToken(refresh_str)
            jti = rt.get('jti')
        except Exception:
            return Response({'detail': 'Refresh token invalide.'}, status=status.HTTP_400_BAD_REQUEST)

        # Lookup stored token by jti or raw token
        stored = None
        if jti:
            stored = StoredRefreshToken.objects.filter(jti=jti).first()
        if not stored:
            stored = StoredRefreshToken.objects.filter(refresh_token=refresh_str).first()

        if not stored:
            response = Response({'detail': 'Refresh token non reconnu.'}, status=status.HTTP_401_UNAUTHORIZED)
            response.delete_cookie('refresh_token')
            response.delete_cookie('authenticated')
            return response

        if stored.revoked:
            response = Response({'detail': 'Refresh token révoqué.'}, status=status.HTTP_401_UNAUTHORIZED)
            response.delete_cookie('refresh_token')
            response.delete_cookie('authenticated')
            return response

        if stored.expires_at and stored.expires_at < tz.now():
            response = Response({'detail': 'Refresh token expiré.'}, status=status.HTTP_401_UNAUTHORIZED)
            # Delete cookies if token is expired
            response.delete_cookie('refresh_token')
            response.delete_cookie('authenticated')
            return response

        # Validate & rotate via simplejwt serializer
        serializer = TokenRefreshSerializer(data={'refresh': refresh_str})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        new_refresh = data.get('refresh')
        if new_refresh:
            # rotation: revoke old stored and save new
            try:
                new_rt = RefreshToken(new_refresh)
                new_jti = new_rt.get('jti')
                new_exp = new_rt.get('exp')
                new_expires_at = timezone.datetime.fromtimestamp(new_exp, tz=timezone.utc) if new_exp else None
            except Exception:
                new_jti = None
                new_expires_at = None

            stored.revoked = True
            stored.save()
            StoredRefreshToken.objects.create(
                user=stored.user,
                refresh_token=new_refresh,
                jti=new_jti,
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:512],
                expires_at=new_expires_at,
            )

            # Build response, replace cookies with the new refresh
            response = Response(data, status=status.HTTP_200_OK)
            response.delete_cookie('refresh_token')
            response.delete_cookie('authenticated')
            response.set_cookie(
                'refresh_token',
                new_refresh,
                httponly=True,
                secure=True,
                samesite='Lax',
                max_age=14 * 24 * 60 * 60,
                path='/'
            )
            response.set_cookie(
                'authenticated',
                'true',
                httponly=False,
                secure=True,
                samesite='Lax',
                max_age=14 * 24 * 60 * 60,
            )

            if 'refresh' in response.data:
                del response.data['refresh']
            return response

        # No rotation: strip refresh from payload and return
        if 'refresh' in data:
            del data['refresh']
        return Response(data, status=status.HTTP_200_OK)

