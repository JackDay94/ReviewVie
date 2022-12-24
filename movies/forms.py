from .models import Movie, Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = (
            "review_content",
            "rating",
        )
