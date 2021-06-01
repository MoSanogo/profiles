from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .serializers import UserProfileSerializer,TweetSerializer,CommentSerializer
from .models import UserProfile,Tweet,Comment
from .permissions import UpdateOwnProfile,UpdateOwnTweet,UpdateOwnComment
from django.shortcuts import get_object_or_404



class UserProfileViewSet(ModelViewSet):
    """Handles creating and updating a user profile"""
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()
    permission_classes=(UpdateOwnProfile,IsAuthenticatedOrReadOnly)
    authentication_classes=(TokenAuthentication,)
    filter_backends=(filters.SearchFilter,)
    search_fields=("name","email")
    
    def create(self, request, *args, **kwargs):
        """Create a model instance."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user=UserProfile.objects.filter(email=serializer.data["email"]).first()
        token=Token.objects.create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response({**serializer.data,"token":token.key}, status=status.HTTP_201_CREATED, headers={**headers,"token":token.key})

class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class TweetViewSet(ModelViewSet):
    """Creating,reading tweets"""
    permission_classes=(UpdateOwnTweet,IsAuthenticatedOrReadOnly,)
    authentication_classes=(TokenAuthentication,)
    serializer_class=TweetSerializer
    queryset=Tweet.objects.all()
    filter_backends=(filters.SearchFilter,)
    search_fields=("author","created_at","updated_at",)
    def perform_create(self,serializer):
        """Sets the author of the tweet"""
        serializer.save(author=self.request.user)



class CommentViewSet(ModelViewSet):
    """Creating,reading tweets"""
    authentication_classes=(TokenAuthentication,)
    permission_classes=(UpdateOwnComment,IsAuthenticatedOrReadOnly,)
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()
    search_fields=("author","created_at","updated_at","tweet")
    def perform_create(self,serializer):
        """Sets the author of the tweet"""
        commented_tweet= get_object_or_404(Tweet,pk=serializer.validated_data["tweet"].id )
        serializer.save(author=self.request.user,tweet=commented_tweet)
