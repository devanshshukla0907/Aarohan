from rest_framework import serializers
from .models import UserProfile, SocialMediaDetail, Competition, AthleteVideo

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class SocialMediaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaDetail
        fields = '__all__'

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

class AthleteVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteVideo
        fields = '__all__'
