from django.urls import path
from .views import MoviesHome

urlpatterns = [
    path('', MoviesHome.as_view(), name='home'),
]
