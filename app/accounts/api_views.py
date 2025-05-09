from rest_framework import status, viewsets
from django.contrib.auth import  logout
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.decorators import action
from accounts.models import User

from accounts.serializers import *
from rest_framework import filters
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    

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
    permission_classes = []
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "username",
        "email"
        
    ]
    ordering_fields = [
        "username",
        "email"
      
    ]

    @action(detail=False,url_path='logout')
    def logout_user(self, request):
        logout(request)
        response = {
            "status": status.HTTP_200_OK,
            "message": "success",
        }
        return Response(response, status=status.HTTP_200_OK)
    

class AdminViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.filter(is_superuser=True)
    serializer_class = AdminSerializer
    permission_classes = [IsSuperUser,]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "username",
        "email"
        
    ]
    ordering_fields = [
        "username",
        "email"
      
    ]

