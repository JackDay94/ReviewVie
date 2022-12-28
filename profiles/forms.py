from .models import Profile
from django.forms import ModelForm


class ProfileForm(ModelForm):
    """
    Displays the user profile form.
    """
    class Meta:
        model = Profile
        fields = (
            "age",
            "favourite_genre",
            "favourite_director",
        )
