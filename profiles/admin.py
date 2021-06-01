from django.contrib import admin
from .models import UserProfile,Tweet,Comment
# Register your models here.
admin.site.register([UserProfile,Tweet,Comment])