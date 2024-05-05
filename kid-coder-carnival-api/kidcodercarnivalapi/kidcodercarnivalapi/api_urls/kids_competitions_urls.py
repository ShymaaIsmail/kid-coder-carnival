from django.urls import path
from ..views import (
    NewCurrentCompetitionList,
    CreateCompetitionParticipant
)

urlpatterns = [
    path('open-competitions', NewCurrentCompetitionList.as_view(), name='get-open-current-competition'),
    path('participate-competition', CreateCompetitionParticipant.as_view(), name='participate-competition'),
    path('start-competition', NewCurrentCompetitionList.as_view(), name='start-competition'),
    path('submit-competition', NewCurrentCompetitionList.as_view(), name='submit-competition'),
    path('previous-competitions', NewCurrentCompetitionList.as_view(), name='participate-competition'),
]
