from django.http import JsonResponse
from .base_api_view import BaseAPIView
from ..services.user_service import UserService

class UserView(BaseAPIView):

    def  __init__(self):
        super().__init__()
        self.user_service = UserService()
