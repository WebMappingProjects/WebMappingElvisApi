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
from django.utils import timezone


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
            # fallback: try to get user by username from response data or request data
            username = response.data.get('username') or request.data.get('username') or request.data.get('email')
            if username:
                user = User.objects.filter(username=username).first() or User.objects.filter(email=username).first()

        if user:
            # Revoke all previous refresh tokens for this user
            StoredRefreshToken.objects.filter(user=user, revoked=False).update(revoked=True)

        # Remove all revoked refresh tokens for this user
        if user:
            # Supprimer tous les tokens dont la date d'expiration est déjà dépassée
            StoredRefreshToken.objects.filter(expires_at__lt=timezone.now()).delete()

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
                user=request.user if request.user and request.user.is_authenticated else User.objects.filter(username=response.data.get('username')).first(),
                refresh_token=refresh_token,
                jti=jti,
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:512],
                expires_at=expires_at,
            )

        return response


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh),
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

            return Response(response_data, status=status.HTTP_201_CREATED)
        
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

    @action(detail=False, url_path='logout', permission_classes=[permissions.IsAuthenticated])
    def logout_user(self, request):
        logout(request)
        response = {
            "status": status.HTTP_200_OK,
            "message": "success",
        }
        return Response(response, status=status.HTTP_200_OK)
    
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
        # vérifier que le refresh token est connu et non révoqué
        refresh_str = request.data.get('refresh')
        if not refresh_str:
            return Response({'detail': 'Refresh token manquant.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            rt = RefreshToken(refresh_str)
            jti = rt.get('jti')
        except Exception:
            return Response({'detail': 'Refresh token invalide.'}, status=status.HTTP_400_BAD_REQUEST)

        stored = None
        if jti:
            stored = StoredRefreshToken.objects.filter(jti=jti).first()
        if not stored:
            stored = StoredRefreshToken.objects.filter(refresh_token=refresh_str).first()

        if not stored:
            return Response({'detail': 'Refresh token non reconnu.'}, status=status.HTTP_401_UNAUTHORIZED)

        if stored.revoked:
            return Response({'detail': 'Refresh token révoqué.'}, status=status.HTTP_401_UNAUTHORIZED)

        if stored.expires_at and stored.expires_at < timezone.now():
            return Response({'detail': 'Refresh token expiré.'}, status=status.HTTP_401_UNAUTHORIZED)

        # valide via serializer simplejwt
        serializer = TokenRefreshSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # si rotation activée, remplacer le refresh stocké
        new_refresh = data.get('refresh')
        if new_refresh:
            try:
                new_rt = RefreshToken(new_refresh)
                new_jti = new_rt.get('jti')
                new_exp = new_rt.get('exp')
                new_expires_at = timezone.datetime.fromtimestamp(new_exp, tz=timezone.utc) if new_exp else None
            except Exception:
                new_jti = None
                new_expires_at = None

            # marquer l'ancien comme révoqué et enregistrer le nouveau
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

        return Response(data, status=status.HTTP_200_OK)

