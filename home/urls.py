from django.urls import path
from .views import MoviesHome, MovieList, MovieSearch

urlpatterns = [
    path('', MoviesHome.as_view(), name='home'),
    path('all-movies/', MovieList.as_view(), name='all-movies'),
    path('search-result/', MovieSearch.as_view(), name='search-result'),
]
