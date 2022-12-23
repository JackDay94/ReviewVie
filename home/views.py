from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.http import HttpResponse
from movies.models import Movie, Review


class MoviesHome(ListView):
    model = Movie, Review
    template_name = 'home/home.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = {
            'top_movie': Movie.objects.filter(approved=True).order_by(
                '-average_stars')[:1],
            'top_rated': Movie.objects.filter(approved=True).order_by(
                '-average_stars')[1:5],
            'new_release': Movie.objects.filter(approved=True).order_by(
                '-release_date')[:4],
            'new_review': Review.objects.order_by('-created_on')[:4],
        }
        return queryset


class MovieList(ListView):
    model = Movie
    template_name = 'home/all-movies.html'
    context_object_name = 'movies'
    paginate_by = 16


class MovieSearch(ListView):
    model = Movie
    template_name = 'home/all-movies.html'
    context_object_name = 'movies'

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Movie.objects.filter(name__icontains=query) | Movie.objects.filter(director__icontains=query) | Movie.objects.filter(genre__icontains=query)


class MovieFilter(ListView):
    model = Movie
    template_name = 'home/all-movies.html'
    context_object_name = 'movies'
