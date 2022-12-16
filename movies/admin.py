from django.contrib import admin
from .models import Movies


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'genre',
        'director',
        'release_date',
        'age_rating',
        'average_stars'
        )
    list_filter = (
        'genre',
        'director',
        'age_rating',
        'average_stars'
        )
    search_fields = [
        'genre',
        'director',
        ]
