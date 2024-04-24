from django.urls import path
from ..views import (
    CreateListCompetitionAPIView,
    AssignChallengeToCompetitionAPIView,
    ViewCompetitionDetailsAPIView
)

urlpatterns = [
    path('', CreateListCompetitionAPIView.as_view(), name='create-competition'),
    path('<int:competition_id>/challenges/', AssignChallengeToCompetitionAPIView.as_view(), name='assign-challenge-to-competition'),
    path('<int:competition_id>/', ViewCompetitionDetailsAPIView.as_view(), name='view-competition-details'),
    path('<int:competition_id>/participants/', ViewCompetitionDetailsAPIView.as_view(), name='view-participants'),
]
