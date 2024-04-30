from rest_framework import serializers
from .challenge_serializer import ChallengeSerializer
from .user_serializer import UserSerializer
from ..models import Competition, CompetitionChallenge, CompetitionParticipant



class CompetitionParticipantSerializer(serializers.ModelSerializer):
    competition = serializers.PrimaryKeyRelatedField(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = CompetitionParticipant
        fields = ['id', 'competition', 'user', 'registration_date', 'submission_date', 'score', 'rank']

class CompetitionChallengeSerializer(serializers.ModelSerializer):
    competition = serializers.PrimaryKeyRelatedField(read_only=True)
    challenge = ChallengeSerializer(read_only=True)
    class Meta:
        model = CompetitionChallenge
        fields = ['id', 'competition', 'challenge']

class CompetitionSerializer(serializers.ModelSerializer):
    challenges = CompetitionChallengeSerializer(many=True, source='competition_challenges', required=False)
    participants = CompetitionParticipantSerializer(many=True, source='competition_participants', required=False)
    class Meta:
        model = Competition
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'challenges', 'participants']
