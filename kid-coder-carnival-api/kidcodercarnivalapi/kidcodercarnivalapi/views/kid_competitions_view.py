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
        competitions = Competition.objects.filter(
            start_date__date__lte=today,
            end_date__date__gte=today,
            is_complete= False
            ).exclude(
            id__in=enrolled_competitions
        ).distinct()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)

class CreateCompetitionParticipant(BaseKidView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'competition_id': openapi.Schema(type=openapi.TYPE_INTEGER)
            }
        )
    )
    def post(self, request):
        competition_id = request.data.get('competition_id', 0)
        competition = get_object_or_404(Competition.objects, id=competition_id)
        already_enrolled = CompetitionParticipant.objects.filter(
            user_id= request.user.id,
            competition_id= competition_id)
        if already_enrolled:
            return Response({'message': 'Sorry, you are already enrolled in this competition'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            CompetitionParticipant.objects.create(competition=competition, user=request.user)
            return Response({'message': f'You are now participated in Competition {competition.title}'}, status=status.HTTP_200_OK)

class  InProgressCompetitionList(BaseKidView):
    def get(self, request):
        enrolled_competitions = CompetitionParticipant.objects.filter(
            user_id= request.user.id
            ).values_list(
                'competition_id', flat=True
            )
        competitions = Competition.objects.filter(
            is_complete= False,
            id__in=enrolled_competitions
            ).distinct()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)


class  CompletedCompetitionList(BaseKidView):
    def get(self, request):
        enrolled_competitions = CompetitionParticipant.objects.filter(
            user_id= request.user.id
            ).values_list(
                'competition_id', flat=True
            )
        competitions = Competition.objects.filter(
            is_complete= True,
            id__in=enrolled_competitions
            ).distinct()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data)

class  StartCompetition(BaseKidView):
    def get(self, request, competition_id):
        already_enrolled = get_object_or_404(CompetitionParticipant, user_id= request.user.id,
        competition_id= competition_id)
        if (already_enrolled):
            competition = get_object_or_404(Competition.objects.prefetch_related('competition_challenges'),
                                            id=competition_id, is_complete= False)
            serializer = CompetitionSerializer(competition)
            serialized_data = serializer.data.copy()
            serialized_data.pop("participants", None)
            return Response(serialized_data)

class  SubmitCompetition(BaseKidView):
    def post(self, request):
        pass
