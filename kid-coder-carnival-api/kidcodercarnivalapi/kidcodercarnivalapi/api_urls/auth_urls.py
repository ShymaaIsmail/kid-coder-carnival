from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from ..views import auth_views

urlpatterns = [
    path('admin/login/', obtain_auth_token, name='admin_login'),
    path('get_user/', auth_views.UserView.as_view(), name='get_user'),
]
