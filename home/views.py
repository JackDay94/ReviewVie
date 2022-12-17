from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import HttpResponse
from movies.models import Movie


def home(request):
    return HttpResponse('<h1>Hello World!</h1>')
