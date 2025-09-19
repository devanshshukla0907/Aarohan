from rest_framework import viewsets
from .models import UserProfile, SocialMediaDetail, Competition, AthleteVideo
from .serializers import UserProfileSerializer, SocialMediaDetailSerializer, CompetitionSerializer, AthleteVideoSerializer
from rest_framework.permissions import IsAuthenticated

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class SocialMediaDetailViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaDetail.objects.all()
    serializer_class = SocialMediaDetailSerializer
    permission_classes = [IsAuthenticated]

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAuthenticated]

class AthleteVideoViewSet(viewsets.ModelViewSet):
    queryset = AthleteVideo.objects.all()
    serializer_class = AthleteVideoSerializer
    permission_classes = [IsAuthenticated]
