from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..views.base_api_view import BaseAPIView
from ..models import Competition, Challenge, User
from ..serializers.competition_serializer import CompetitionSerializer

class CreateListCompetitionAPIView(BaseAPIView):
    def get(self, request):
        competitions = Competition.objects.all()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CompetitionSerializer,
        responses={status.HTTP_201_CREATED: CompetitionSerializer,
                   status.HTTP_400_BAD_REQUEST: CompetitionSerializer}
    )
    def post(self, request):
        serializer = CompetitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignChallengeToCompetitionAPIView(BaseAPIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'challenge_ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_INTEGER))
            }
        )
    )
    def post(self, request, competition_id):
        competition = Competition.objects.get(id=competition_id)
        challenge_ids = request.data.get('challenge_ids', [])
        challenges = Challenge.objects.filter(id__in=challenge_ids)
        competition.challenges.set(challenges)
        return Response({'message': 'Challenges assigned successfully'}, status=status.HTTP_200_OK)

class ViewCompetitionDetailsAPIView(BaseAPIView):
    def get(self, request, competition_id):
        competition = get_object_or_404(Competition.objects.prefetch_related('competitionchallenge_set__challenge'), id=competition_id)
        competition.challenges.set(competition.challenges.all())
        serializer = CompetitionSerializer(competition)
        return Response(serializer.data)


class ViewCompetitionParticipantsAPIView(BaseAPIView):
    def get(self, request, competition_id):
        competition = get_object_or_404(Competition.objects.prefetch_related('competition_participants'), id=competition_id)
        serializer = CompetitionSerializer(competition)
        return Response(serializer.data)
