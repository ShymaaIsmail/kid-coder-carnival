from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Base Protected view class
class BaseAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
