from django.urls import path
from ..views.kid_profile_views import KidProfileView

urlpatterns = [
    path('kid/profile/', KidProfileView.as_view(), name='kid_profile'),
]
