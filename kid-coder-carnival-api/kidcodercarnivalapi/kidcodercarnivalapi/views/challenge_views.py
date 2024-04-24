from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..views.base_api_view import BaseAPIView
from ..models import Challenge
from ..serializers import ChallengeSerializer
from rest_framework.permissions import AllowAny


class ChallengeAPIView(BaseAPIView):

    def get(self, request):
        challenges = Challenge.objects.all()
        serializer = ChallengeSerializer(challenges, many=True)
        return Response(serializer.data)
