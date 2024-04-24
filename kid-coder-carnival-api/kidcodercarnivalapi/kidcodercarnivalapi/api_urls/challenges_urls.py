from django.urls import path
from ..views.challenge_views import (
    ChallengeAPIView,
)

urlpatterns = [
    path('', ChallengeAPIView.as_view(), name='get-all-challenges'),
]
