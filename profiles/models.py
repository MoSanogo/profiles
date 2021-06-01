from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings
from django.utils.text import Truncator

class UserProfileManager(BaseUserManager):
    """Manager for uswer profiles"""
    def _create_user(self,email,name,password,**extra_fields):
        """Create and save a user with a given name,email,password"""
        if not email :
            raise ValueError("User must provide an email")
        
        email=self.normalize_email(email)
        user=self.model(email=email,name=name,**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_user(self,email,name,password,**extra_fields):
        """Create a new user profile"""
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,name,password,**extra_fields)

    def create_superuser(self,email,name,password,**extra_fields):
        """Create a new superuser"""
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)


        user=self._create_user(email,name,password,**extra_fields)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system """
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]

    def __str__(self):
        """"Retrieve string representation of the user"""
        return self.email
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.name



class Tweet(models.Model):
    """Database Model for user's tweets"""
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    message=models.TextField(max_length=4000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        """Returns a string representation of the Comment Model"""
        truncated_message=Truncator(self.message)
        return truncated_message.chars(30)



class Comment(models.Model):
    tweet=models.ForeignKey(Tweet,on_delete=models.CASCADE,null=True)
    comment=models.TextField(max_length=400)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    def __str__(self):
        """Returns a string representation of the Comment Model"""
        truncated_message=Truncator(self.comment)
        return truncated_message.chars(30)


#  


