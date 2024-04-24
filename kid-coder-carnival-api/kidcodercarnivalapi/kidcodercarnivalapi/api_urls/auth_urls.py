from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from ..views import auth_views

urlpatterns = [
    path('admin/login/', TokenObtainPairView.as_view(), name='admin_login'),
    path('get_user/', auth_views.UserView.as_view(), name='get_user'),
]
