from rest_framework import serializers
from ..models import Competition, CompetitionChallenge, CompetitionParticipant

class CompetitionParticipantSerializer(serializers.ModelSerializer):
    competition = serializers.PrimaryKeyRelatedField(read_only=True)
    participant = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CompetitionParticipant
        fields = '__all__'

class CompetitionChallengeSerializer(serializers.ModelSerializer):
    competition = serializers.PrimaryKeyRelatedField(read_only=True)
    challenge = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CompetitionChallenge
        fields = '__all__'
class CompetitionSerializer(serializers.ModelSerializer):
    challenges = CompetitionChallengeSerializer(many=True, read_only=True)
    participants = CompetitionParticipantSerializer(many=True, read_only=True)
    class Meta:
        model = Competition
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'challenges', 'participants']

