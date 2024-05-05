from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .base_kid_view import BaseKidView
from ..models import Competition, CompetitionParticipant
from ..serializers.competition_serializer import CompetitionSerializer

class NewCurrentCompetitionList(BaseKidView):
    def get(self, request):
        today = timezone.now().date()
        enrolled_competitions = CompetitionParticipant.objects.filter(
            user_id= request.user.id
            ).values_list(
                'competition_id', flat=True
                )
        print(enrolled_competitions)
        competitions = Competition.objects.filter(
            start_date__date__lte=today,
            end_date__date__gte=today
            ).exclude(
            id__in=enrolled_competitions
        ).distinct()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)
