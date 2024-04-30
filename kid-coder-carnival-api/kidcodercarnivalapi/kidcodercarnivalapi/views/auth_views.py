from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from ..serializers import UserRegistrationSerializer
class KidAuthView(APIView):

    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        responses={status.HTTP_201_CREATED: UserRegistrationSerializer,
                   status.HTTP_400_BAD_REQUEST: UserRegistrationSerializer}
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


