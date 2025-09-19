from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, SocialMediaDetailViewSet, CompetitionViewSet, AthleteVideoViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'socialmedia', SocialMediaDetailViewSet)
router.register(r'competitions', CompetitionViewSet)
router.register(r'athletevideos', AthleteVideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
