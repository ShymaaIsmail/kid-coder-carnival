from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from ..models.user import User
from .base_kid_view import BaseKidView
from ..serializers import UserSerializer

class KidProfileView(BaseKidView):

    @swagger_auto_schema(
        responses={status.HTTP_201_CREATED: UserSerializer,
                status.HTTP_400_BAD_REQUEST: UserSerializer}
    )
    def get(self, request):
        user_id = request.user.id
        print(user_id)
        user_profile = get_object_or_404(User, id= user_id)
        serializer = UserSerializer(user_profile)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body= UserSerializer,
        responses={status.HTTP_201_CREATED: UserSerializer,
                status.HTTP_400_BAD_REQUEST: UserSerializer}
    )
    def put(self, request):
        user_id = request.user.id
        user_profile = get_object_or_404(User, id= user_id)
        serializer = UserSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

