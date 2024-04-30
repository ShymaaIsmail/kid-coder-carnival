from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Base Protected view class
class BaseAdminView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
