from .models import Review, Movie
from django.forms import ModelForm, DateInput


class DateInput(DateInput):
    input_type = 'date'


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = (
            "rating",
            "review_content",
        )


class AddMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = (
            "name",
            "genre",
            "release_date",
            "director",
            "age_rating",
            "summary",
            "image",
        )
        widgets = {'release_date': DateInput()}
