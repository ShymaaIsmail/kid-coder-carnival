from rest_framework.permissions import BasePermission

class AllowUnauthenticatedForSomeAPIs(BasePermission):
    """
    Custom permission class to allow unauthenticated access to Swagger UI.
    and kid user register api
    """

def has_permission(self, request, view):
    paths_to_check = ['/swagger/', '/redoc/']  
    for path in paths_to_check:
        if request.path.startswith(path):
            return True
    return False
