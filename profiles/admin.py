"""Admin for the Profiles App"""
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Class which handles what the admin can see from
    the admin dashboard of the Profile model and what
    can be filtered and searched.
    """
    list_display = ('user', 'favourite_genre', 'favourite_director', 'age')
    list_filter = ('user', 'favourite_genre', 'favourite_director')
    search_fields = ['user__username',]
