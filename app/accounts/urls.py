from rest_framework import routers
from accounts.api_views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "accounts"

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'admins', AdminViewSet, basename='admins')
router.register(r'', TokenViewSet, basename='refresh')


urlpatterns = router.urls

urlpatterns += [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    # path('refresh/', TokenViewSet.as_view(), name='refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
