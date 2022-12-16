from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from cloudinary.models import CloudinaryField


class Movies(models.Model):

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    genre = models.CharField(
        choices=Profile.Genre.choices, max_length=50, blank=True, default=''
        )
    release_date = models.DateField()
    director = models.CharField(max_length=50)
    age_rating = models.IntegerField()
    summary = models.TextField(max_length=1000)
    image = CloudinaryField("movie image", default="placeholder_image")
    average_stars = models.FloatField()

    def __str__(self):
        return f"{self.name}"
