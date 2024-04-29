from rest_framework import serializers

from .challenge_serializer import ChallengeSerializer
from ..models import Competition, CompetitionChallenge, CompetitionParticipant, User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login']
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
    challenges = CompetitionChallengeSerializer(many=True, read_only=True)
    participants = CompetitionParticipantSerializer(many=True, read_only=True)
    class Meta:
        model = Competition
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'challenges', 'participants']

