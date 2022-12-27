from django.urls import path
from .views import (
     MovieDetail, UpdateReview, DeleteReview, AddMovie, UpdateMovie
     )


urlpatterns = [
     path('add_movie/', AddMovie.as_view(), name='add_movie'),
     path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
     path('<slug:slug>/update_movie/', UpdateMovie.as_view(),
          name='update_movie'),
     path('<int:pk>/update_review/', UpdateReview.as_view(),
          name='update_review'),
     path('<int:pk>/delete_review/', DeleteReview.as_view(),
          name='delete_review'),
]
