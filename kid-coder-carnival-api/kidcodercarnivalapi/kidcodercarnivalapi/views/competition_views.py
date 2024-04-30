from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .base_admin_view import BaseAdminView
from ..models import Competition, Challenge, CompetitionChallenge
from ..serializers.competition_serializer import CompetitionSerializer

class CreateListCompetitionAPIView(BaseAdminView):
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

class AssignChallengeToCompetitionAPIView(BaseAdminView):
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
        # Clear existing challenges associated with the competition
        competition.challenges.clear()
        # Create new CompetitionChallenge instances for each selected challenge
        for challenge in challenges:
            CompetitionChallenge.objects.create(competition=competition, challenge=challenge)
        return Response({'message': 'Challenges assigned successfully'}, status=status.HTTP_200_OK)

class ViewCompetitionDetailsAPIView(BaseAdminView):
    def get(self, request, competition_id):
        competition = get_object_or_404(Competition.objects.prefetch_related('competition_challenges'), id=competition_id)
        print(vars(competition))
        serializer = CompetitionSerializer(competition)
        serialized_data = serializer.data.copy()
        serialized_data.pop("participants", None)
        return Response(serialized_data)


class ViewCompetitionParticipantsAPIView(BaseAdminView):
    def get(self, request, competition_id):
        competition = get_object_or_404(Competition.objects.prefetch_related('competition_participants'), id=competition_id)
        serializer = CompetitionSerializer(competition)
        return Response(serializer.data["participants"])
