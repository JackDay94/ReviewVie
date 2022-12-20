from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.http import HttpResponse
from movies.models import Movie


class TopMovie(ListView):
    model = Movie
    template_name = 'home/home.html'
    queryset = Movie.objects.filter(approved=True).order_by(
        '-average_stars')[:1]

# def home(request):
#     return render(request, 'home/home.html')
