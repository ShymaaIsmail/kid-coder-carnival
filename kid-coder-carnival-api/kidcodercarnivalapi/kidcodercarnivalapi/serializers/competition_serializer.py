from rest_framework import serializers
from .challenge_serializer import ChallengeSerializer
from .user_serializer import UserSerializer
from ..models import Competition, CompetitionChallenge, CompetitionParticipant



class CompetitionParticipantSerializer(serializers.ModelSerializer):
    competition = serializers.PrimaryKeyRelatedField(# In the provided code snippet, `read_only=True`
    # is used in the serializers to specify that the
    # field is read-only and should not be included
    # in the serialized data when the serializer is
    # used for deserialization (parsing input data)
    # or updating instances.
    read_only=True)
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
    is_complete  = serializers.ReadOnlyField()
    challenges = CompetitionChallengeSerializer(many=True, source='competition_challenges', required=False, read_only=True)
    participants = CompetitionParticipantSerializer(many=True, source='competition_participants', required=False, read_only=True)
    class Meta:
        model = Competition
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'is_complete', 'challenges', 'participants']
