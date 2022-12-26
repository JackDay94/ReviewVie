from django.urls import path
from .views import MovieDetail, UpdateReview


urlpatterns = [
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
    path('<int:pk>/update_review/', UpdateReview.as_view(),
         name='update_review'),
]
