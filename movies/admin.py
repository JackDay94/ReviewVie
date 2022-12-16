from django.contrib import admin
from .models import Movie, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'genre',
        'director',
        'release_date',
        'age_rating',
        'average_stars',
        'approved'
        )
    list_filter = (
        'genre',
        'director',
        'age_rating',
        'average_stars',
        'approved'
        )
    search_fields = [
        'name',
        'genre',
        'director',
        ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'movie',
        'rating',
        'created_on'
    )
    list_filter = (
        'created_on',
        'movie__name'
    )
    search_fields = [
        'author',
        'movie',
    ]
