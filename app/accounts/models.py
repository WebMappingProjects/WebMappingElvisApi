from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('decideur', 'Décideur'),
        ('technicien', 'Technicien'),
        ('lambda', 'Utilisateur Lambda'),
    )
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='lambda',
        verbose_name='Rôle'
    )
    
    code = models.CharField(null=True, blank=True)
    code_expires_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'


class StoredRefreshToken(models.Model):
    """Stocke les refresh tokens émis pour un utilisateur.

    On garde le token (ou son jti) pour pouvoir révoquer des refresh tokens
    côté serveur si nécessaire.
    """
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='refresh_tokens')
    refresh_token = models.TextField()
    jti = models.CharField(max_length=255, blank=True, null=True, help_text='JWT ID (optionnel)')
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(blank=True, null=True)
    revoked = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Refresh token stocké'
        verbose_name_plural = 'Refresh tokens stockés'
        ordering = ['-created_at']

    def __str__(self):
        return f"RefreshToken(user={self.user.username}, revoked={self.revoked}, created={self.created_at.isoformat()})"

