from django.urls import path
from ..views import auth_views

urlpatterns = [
    path('get_user/', auth_views.UserView.as_view(), name='get_user'),
]
