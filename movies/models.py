from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from profiles.consts import GENRE, AGE_RATING, MOVIE_RATING
from cloudinary.models import CloudinaryField


class Movie(models.Model):
    """
    Movie model which contains details of movies
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    genre = models.CharField(
        choices=GENRE, max_length=50, blank=True, default=''
        )
    release_date = models.DateField()
    director = models.CharField(max_length=50)
    age_rating = models.CharField(
        choices=AGE_RATING, max_length=50, blank=True, default=''
        )
    summary = models.TextField(max_length=1000)
    image = CloudinaryField("movie image", default="placeholder_image")
    average_stars = models.FloatField(default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def update_review_fields(self):
        """
        Updates the average_star field depending on average user rating.
        Taken from:
        https://www.reddit.com/r/django/comments/kp6rz4/which_is_the_proper_way_of_calculating_average/
        """
        reviews = self.reviews.all()
        self.average_stars = reviews.aggregate(models.Avg('rating')).get(
            'rating__avg'
            )
        self.save(update_fields=['average_stars'])


class Review(models.Model):
    """
    Review model used for user reviews on movies
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="reviews"
        )
    review_content = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=MOVIE_RATING, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review of {self.movie} by {self.author}"

    def save(self, *args, **kwargs):
        """
        Overwrites the save method in Review and calls update_review_fields
        method after saving the object.
        Taken from:
        https://www.reddit.com/r/django/comments/kp6rz4/which_is_the_proper_way_of_calculating_average/
        """
        super(Review, self).save(*args, **kwargs)
        self.movie.update_review_fields()
