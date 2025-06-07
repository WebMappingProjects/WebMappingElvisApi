from rest_framework import status, viewsets
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.decorators import action
from accounts.models import User
from accounts.serializers import *
from accounts.permissions import *
from rest_framework import filters
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


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