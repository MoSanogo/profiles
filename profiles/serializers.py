from rest_framework import serializers
from .models import UserProfile,Tweet,Comment

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile model object"""
    
    class Meta:
        model=UserProfile
        fields=("id","email","name","password")
        extra_kwargs={
            "password":{
                "write_only":True,
                "style":{
                    "input_type":"password"
                }
            }
        }
    def create(self,validated_data):
        """Create and return a new user"""
        user=UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"]
        )
        return user


class TweetSerializer(serializers.ModelSerializer):
    """Serializes user tweets"""
    
    class Meta:
        model=Tweet
        fields=("id", "author","created_at","updated_at","message")
        extra_kwargs={
            "author":{
                "read_only":True
            }
        }


class CommentSerializer(serializers.ModelSerializer):
    """Serializes user comments"""

    class Meta:
        model=Comment
        fields=("id", "author","created_at","updated_at","comment","tweet")
        extra_kwargs={
            "author":{
                "read_only":True
            },
            "tweet":{
               "required":True,
               "write_only":True
            },

        }
