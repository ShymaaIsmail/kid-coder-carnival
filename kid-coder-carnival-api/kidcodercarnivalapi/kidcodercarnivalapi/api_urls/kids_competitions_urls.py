from django.urls import path
from ..views import (
    NewCurrentCompetitionList,
    CreateCompetitionParticipant,
    InProgressCompetitionList,
    StartCompetition,
    SubmitCompetition,
    CompletedCompetitionList
)

urlpatterns = [
    path('available-competitions', NewCurrentCompetitionList.as_view(), name='get-available-current-competition'),
    path('participate-competition', CreateCompetitionParticipant.as_view(), name='participate-competition'),
    path('in-progress-competitions', InProgressCompetitionList.as_view(), name='participate-competition'),
    path('start-competition/<int:competition_id>', StartCompetition.as_view(), name='start-competition'),
    path('submit-competition', SubmitCompetition.as_view(), name='submit-competition'),
    path('completed-competitions', CompletedCompetitionList.as_view(), name='participate-competition'),
]
