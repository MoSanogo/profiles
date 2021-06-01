from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet,UserLoginApiView,TweetViewSet,CommentViewSet

router = DefaultRouter()
router.register("profile",UserProfileViewSet)
router.register("tweet",TweetViewSet)
router.register("comment",CommentViewSet)

app_name="profiles"

urlpatterns = [
    path("",include(router.urls),),
    path("login/", UserLoginApiView.as_view(),)
]
