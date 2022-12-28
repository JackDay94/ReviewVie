from .models import Review, Movie
from django.forms import ModelForm, DateInput


class DateInput(DateInput):
    """
    Displays an input as a date field.
    """
    input_type = 'date'


class ReviewForm(ModelForm):
    """
    Displays the review form.
    """
    class Meta:
        model = Review
        fields = (
            "rating",
            "review_content",
        )


class AddMovieForm(ModelForm):
    """
    Displays the Movie form for adding
    new movies.
    """
    class Meta:
        model = Movie
        fields = (
            "name",
            "genre",
            "release_date",
            "director",
            "age_rating",
            "summary",
        )
        widgets = {'release_date': DateInput()}


class UpdateMovieForm(ModelForm):
    """
    Displays the movie form for updating
    existing movies.
    """
    class Meta:
        model = Movie
        fields = (
            "name",
            "genre",
            "release_date",
            "director",
            "age_rating",
            "summary",
        )
        widgets = {'release_date': DateInput()}
