from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model which extends the User model
    """
    class Genre(models.TextChoices):
        """
        Choices for the Genre field
        """
        ACT = 'Action', 'Action'
        ADV = 'Adventure', 'Adventure'
        COM = 'Comedy', 'Comedy'
        CRI = 'Crime', 'Crime'
        DRA = 'Drama', 'Drama'
        FAM = 'Family', 'Family'
        FAN = 'Fantasy', 'Fantasy'
        HOR = 'Horror', 'Horror'
        MUS = 'Music', 'Music'
        ROM = 'Romance', 'Romance'
        SCI = 'Sci-Fi', 'Sci-Fi'
        SPT = 'Sport', 'Sport'
        SUP = 'Superhero', 'Superhero'
        THR = 'Thriller', 'Thriller'
        WAR = 'War', 'War'
        WST = 'Western', 'Western'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_genre = models.CharField(
        choices=Genre.choices, max_length=50, blank=True, default=''
        )
    favourite_director = models.CharField(
        max_length=50, blank=True, default=''
        )
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user}"
