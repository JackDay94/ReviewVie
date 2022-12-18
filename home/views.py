from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.http import HttpResponse
from movies.models import Movie


def home(request):
    return HttpResponse('<h1>ReviewVie Home</h1>')
