from django.urls import path
from .views import TopMovie

urlpatterns = [
    path('', TopMovie.as_view(), name='home'),
]
