from rest_framework.permissions import BasePermission

class AllowUnauthenticatedForSomeAPIs(BasePermission):
    """
    Custom permission class to allow unauthenticated access to Swagger UI.
    and kid user register api
    """

    def has_permission(self, request, view):
        # Check if the request is for the Swagger UI URL(s)
        return request.path.startswith('/swagger/')
