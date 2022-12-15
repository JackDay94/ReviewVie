from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model
    """
    class Genre(models.TextChoices):
        """
        Choices for the Genre field
        """
        NP = 'NP', 'No Preference'
        ACT = 'ACT', 'Action'
        ADV = 'ADV', 'Adventure'
        COM = 'COM', 'Comedy'
        CRI = 'CRI', 'Crime'
        DRA = 'DRA', 'Drama'
        FAM = 'FAM', 'Family'
        FAN = 'FAN', 'Fantasy'
        HOR = 'HOR', 'Horror'
        MUS = 'MUS', 'Music'
        ROM = 'ROM', 'Romance'
        SCI = 'SCI', 'Sci-Fi'
        SPT = 'SPT', 'Sport'
        SUP = 'SUP', 'Superhero'
        THR = 'THR', 'Thriller'
        WAR = 'WAR', 'War'
        WST = 'WST', 'Western'

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
