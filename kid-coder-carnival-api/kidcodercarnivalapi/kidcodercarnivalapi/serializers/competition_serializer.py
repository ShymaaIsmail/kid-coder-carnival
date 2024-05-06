from rest_framework import serializers
from .challenge_serializer import ChallengeSerializer
from .user_serializer import UserSerializer
from ..models import Competition, CompetitionChallenge, CompetitionParticipant, User



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
    is_complete  = serializers.ReadOnlyField()
    challenges = CompetitionChallengeSerializer(many=True, source='competition_challenges', required=False, read_only=True)
    participants = serializers.SerializerMethodField()
    class Meta:
        model = Competition
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'is_complete', 'challenges', 'participants']

    def get_participants(self, obj):
        request = self.context.get('request')
        if request and not request.user.is_staff:
            user_id = request.user.id
            participant = obj.competition_participants.filter(user_id=user_id).first()
            if participant:
                return CompetitionParticipantSerializer(participant).data
        return list(obj.competition_participants.values())  # Return list of participant data directly

