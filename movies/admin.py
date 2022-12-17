"""Admin for the movies App"""
from django.contrib import admin
from .models import Movie, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):
    """
    Class which handles what the admin can see from
    the admin dashboard of the Movie model and what
    can be filtered and searched.
    """
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
    prepopulated_fields = {
        'slug': ('name',)
    }
    summernote_fields = ('summary')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Class which handles what the admin can see from
    the admin dashboard of the Review model and what
    can be filtered and searched.
    """
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
    summernote_fields = ('review_content')
