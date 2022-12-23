from django.urls import path
from .views import MovieDetail


urlpatterns = [
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
]
