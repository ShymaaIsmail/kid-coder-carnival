from rest_framework import serializers

class AnswerSerializer(serializers.Serializer):
    challenge_id = serializers.IntegerField()
    answer = serializers.CharField(max_length=100)

class SubmitCompetitionSerializer(serializers.Serializer):
    competition_id = serializers.IntegerField()
    answers = serializers.ListField(child=AnswerSerializer())
