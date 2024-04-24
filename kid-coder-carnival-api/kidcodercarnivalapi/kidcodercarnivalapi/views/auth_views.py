from django.http import JsonResponse
from .base_api_view import BaseAPIView
from ..services.user_service import UserService

class UserView(BaseAPIView):

    def  __init__(self):
        super().__init__()
        self.user_service = UserService()

    def get(self, request):
        user_id = request.GET.get('user_id')
        user_data = self.user_service.get_user_data(user_id)
        return JsonResponse(user_data)
