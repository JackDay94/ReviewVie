from django.shortcuts import render
from django.views.generic import UpdateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm


class ProfileView(LoginRequiredMixin, UpdateView):
    """
    Checks the user is logged in and displays the user profile
    and allows them to update it with fields from the ProfileForm.
    Displays a success message when they update successfully.
    """
    model = Profile
    form_class = ProfileForm
    template_name = "profiles/profile.html"
    success_message = "Your profile has been updated successfully!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy("profile_detail", kwargs={"pk": self.object.id})
