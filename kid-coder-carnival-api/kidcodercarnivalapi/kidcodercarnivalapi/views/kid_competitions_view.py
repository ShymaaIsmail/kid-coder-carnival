from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .base_kid_view import BaseKidView
from ..models import Competition, CompetitionParticipant, Challenge
from ..serializers.competition_serializer import CompetitionSerializer
from ..serializers.submit_competition_serializer import SubmitCompetitionSerializer

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
        serializer = CompetitionSerializer(competitions, many=True, context={'request': request})
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
        serializer = CompetitionSerializer(competitions, many=True, context={'request': request})
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
        serializer = CompetitionSerializer(competitions, many=True, context={'request': request})
        return Response(serializer.data)

class  StartCompetition(BaseKidView):
    def get(self, request, competition_id):
        already_enrolled = get_object_or_404(CompetitionParticipant, user_id= request.user.id,
        competition_id= competition_id)
        if (already_enrolled):
            competition = get_object_or_404(Competition.objects.prefetch_related('competition_challenges'),
                                            id=competition_id, is_complete= False)
            serializer = CompetitionSerializer(competition, context={'request': request})
            return Response(serializer.data)

class  SubmitCompetition(BaseKidView):
    @swagger_auto_schema(
        request_body=SubmitCompetitionSerializer,
        responses={200: openapi.Response('Success', schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'percentage_result': openapi.Schema(type=openapi.TYPE_NUMBER),
                'score': openapi.Schema(type=openapi.TYPE_INTEGER),
                'max_score': openapi.Schema(type=openapi.TYPE_INTEGER)
            }
        ))}
    )
    def post(self, request):
        # Extract data from the request body
        competition_id = request.data.get('competition_id')
        kid_id = request.user.id  # Get kid_id from request's user
        answers = request.data.get('answers', [])
        # Validate the submitted data
        if not all([competition_id, answers]):
            return Response({'error': 'Incomplete data provided'}, status=status.HTTP_400_BAD_REQUEST)
        # Fetch the competition object or raise 404 if not found
        competition = get_object_or_404(Competition.objects.prefetch_related('competition_challenges'), id=competition_id)
        # Get the participant record
        participant = CompetitionParticipant.objects.get(competition=competition, user_id=kid_id)
        if competition.is_complete is False and \
            participant is not None and participant.submission_date is None:
            # Initialize score and maximum possible score
            score = 0
            max_score = competition.competition_challenges.count()  # Count the number of challenges
            print(max_score)
            # Iterate over each challenge ID and answer
            for answer in answers:
                challenge_id = answer.get('challenge_id')
                kid_answer = answer.get('answer')
                # Fetch the challenge object or raise 404 if not found
                challenge = get_object_or_404(Challenge, id=challenge_id)
                # Fetch the correct answer for the challenge
                correct_answer = challenge.correct_answer
                # Compare the submitted answer with the correct answer
                if kid_answer == correct_answer:
                    # Increment score if the answer is correct
                    score += 1
            # Update the participant's score and submission date
            participant.score = score
            participant.submission_date = timezone.now()
            participant.save()
            # Calculate the final score as a percentage
            percentage_result = (score / max_score) * 100 if max_score > 0 else 0
            # Return the final score and the maximum possible score
            return Response({'percentage_result': percentage_result,
                                'score': score,
                                'max_score': max_score}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Sorry, you are not eligible to submit to this competition'}, status=status.HTTP_400_BAD_REQUEST)
