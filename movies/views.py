from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.http import HttpResponse
from .models import Movie


class MovieDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Movie.objects.filter(approved=True)
        