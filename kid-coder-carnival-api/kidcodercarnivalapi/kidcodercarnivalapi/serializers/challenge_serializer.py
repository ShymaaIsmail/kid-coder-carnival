from rest_framework import serializers
from ..models import Competition, Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'type', 'question', 'options']
