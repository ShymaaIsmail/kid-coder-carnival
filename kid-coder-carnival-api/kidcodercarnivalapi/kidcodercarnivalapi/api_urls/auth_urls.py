from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from ..views.auth_views import KidAuthView

urlpatterns = [
    path('admin/login/', TokenObtainPairView.as_view(), name='admin_login'),
    path('kid/register/', KidAuthView.as_view(), name='kid_register'),
    path('kid/login/', TokenObtainPairView.as_view(), name='kid_login'),
    
    
]
