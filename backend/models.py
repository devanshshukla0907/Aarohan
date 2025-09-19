from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_method = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True)

class SocialMediaDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_media')
    platform = models.CharField(max_length=50)
    profile_url = models.URLField()
    followers_count = models.PositiveIntegerField(default=0)
    engagement_rate = models.FloatField(default=0.0)
    last_updated = models.DateTimeField(auto_now=True)

class Competition(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    registration_open = models.BooleanField(default=True)

class AthleteVideo(models.Model):
    id = models.AutoField(primary_key=True)
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    video_file = models.FileField(upload_to='athlete_videos/')
    competition = models.ForeignKey(Competition, null=True, blank=True, on_delete=models.SET_NULL, related_name='videos')
    task_name = models.CharField(max_length=255)
    upload_time = models.DateTimeField(auto_now_add=True)
    average_rating = models.FloatField(default=0.0)
    rating_count = models.PositiveIntegerField(default=0)
