from django.db import models
from django.contrib.auth.models import User
from .consts import GENRE


class Profile(models.Model):
    """
    Profile model which extends the User model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_genre = models.CharField(
        choices=GENRE, max_length=50, blank=True, default=''
        )
    favourite_director = models.CharField(
        max_length=50, blank=True, default=''
        )
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user}"
