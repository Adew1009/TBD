from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializer import UserProfileSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)


class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            user_profile = get_object_or_404(UserProfile, user=user)
            serializer = UserProfileSerializer(user_profile)

            return Response({'profile': serializer.data, 'username': str(username)})
        except Exception as e:
            return Response({'error': f"Something went wong when retrieving profile: {str(e)}"})


class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            username = user.username
            user_profile = get_object_or_404(UserProfile, user=user)
            ser_profile = UserProfileSerializer(
                user_profile, data=request.data, partial=True)
            if ser_profile.is_valid():
                ser_profile.save()
                return Response({'profile': ser_profile.data, 'username': str(username)})
            return Response(ser_profile.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f"Something went wong when updating profile: {str(e)}"})
