from django.urls import path
from .views import MoviesHome, AllMovies

urlpatterns = [
    path('', MoviesHome.as_view(), name='home'),
    path('all-movies/', AllMovies.as_view(), name='all-movies'),
]
