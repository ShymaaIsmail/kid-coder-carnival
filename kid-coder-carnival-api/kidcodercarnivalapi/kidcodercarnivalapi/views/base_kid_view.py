from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Base Protected view class
class BaseKidView(APIView):
    permission_classes = [IsAuthenticated]
