from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .base_admin_view import BaseAdminView
from ..models import Challenge
from ..serializers import ChallengeSerializer
from rest_framework.permissions import AllowAny


class ChallengeAPIView(BaseAdminView):

    def get(self, request):
        challenges = Challenge.objects.all()
        serializer = ChallengeSerializer(challenges, many=True)
        return Response(serializer.data)
