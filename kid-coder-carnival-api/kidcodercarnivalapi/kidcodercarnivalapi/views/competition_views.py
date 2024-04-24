from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..views.base_api_view import BaseAPIView
from ..models import Competition, Challenge
from ..serializers.competition_serializer import CompetitionSerializer

class CreateListCompetitionAPIView(BaseAPIView):
    def get(self, request):
        competitions = Competition.objects.all()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompetitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignChallengeToCompetitionAPIView(APIView):
    def post(self, request, competition_id):
        competition = Competition.objects.get(id=competition_id)
        challenge_ids = request.data.get('challenge_ids', [])
        challenges = Challenge.objects.filter(id__in=challenge_ids)
        competition.challenges.set(challenges)
        return Response({'message': 'Challenges assigned successfully'}, status=status.HTTP_200_OK)

class ViewCompetitionDetailsAPIView(APIView):
    def get(self, request, competition_id):
        competition = Competition.objects.get(id=competition_id)
        serializer = CompetitionSerializer(competition)
        return Response(serializer.data)
