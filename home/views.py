from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.http import HttpResponse
from movies.models import Movie


class MoviesHome(ListView):
    model = Movie
    template_name = 'home/home.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = {
            'top_movie': Movie.objects.filter(approved=True).order_by(
                '-average_stars')[:1],
            'top_rated': Movie.objects.filter(approved=True).order_by(
                '-average_stars')[:4],
            'new_release': Movie.objects.filter(approved=True).order_by(
                '-release_date')[:4],
        }
        return queryset
