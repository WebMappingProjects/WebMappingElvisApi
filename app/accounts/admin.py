from django.contrib import admin

# Register your models here.
from .models import User, StoredRefreshToken


@admin.register(StoredRefreshToken)
class StoredRefreshTokenAdmin(admin.ModelAdmin):
	list_display = ('user', 'jti', 'revoked', 'created_at', 'expires_at')
	list_filter = ('revoked', 'created_at')
	search_fields = ('user__username', 'jti')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'is_superuser', 'role')
	search_fields = ('username', 'email')
