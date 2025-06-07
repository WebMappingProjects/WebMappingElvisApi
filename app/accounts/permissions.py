from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    L'administrateur a tous les accès
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == 'admin' or request.user.is_superuser
        )

class IsTechnicien(permissions.BasePermission):
    """
    Le technicien peut modifier les tables de données
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # Les techniciens et admins peuvent faire toutes les opérations
        if request.user.role in ['technicien', 'admin'] or request.user.is_superuser:
            return True
        
        # Les décideurs et lambda peuvent seulement lire
        if request.user.role in ['decideur', 'lambda']:
            return request.method in permissions.SAFE_METHODS
        
        return False
    

class TechnicienOrReadOnly(permissions.BasePermission):
    """
    Technicians can edit, others can only read
    """
    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False
        
        if request.method in ['GET', 'HEAD', 'OPTIONS'] and request.user.is_authenticated:
            return True  # Anyone can read
        
        # For write operations, check if user is technician
        return (request.user.is_authenticated and 
                request.user.role in ['technicien', 'admin'] )
    
        
    

class IsDecideurOrAbove(permissions.BasePermission):
    """
    Le décideur et l'utilisateur lambda ont accès en lecture seule
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # Accès lecture seule pour décideur et lambda
        if request.user.role in ['decideur', 'lambda']:
            return request.method in permissions.SAFE_METHODS
        
        # Accès complet pour technicien et admin
        return request.user.role in ['technicien', 'admin'] or request.user.is_superuser

class CanManageUsers(permissions.BasePermission):
    """
    Seul l'administrateur peut gérer les utilisateurs
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == 'admin' or request.user.is_superuser
        )