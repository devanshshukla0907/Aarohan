from django.contrib import admin
from .models import UserProfile, SocialMediaDetail, Competition, AthleteVideo

admin.site.register(UserProfile)
admin.site.register(SocialMediaDetail)
admin.site.register(Competition)
admin.site.register(AthleteVideo)
