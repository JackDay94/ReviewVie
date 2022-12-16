from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from cloudinary.models import CloudinaryField


class Movie(models.Model):

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
    average_stars = models.FloatField(default=0)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_content = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review of {self.movie} by {self.author}"
