from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Movie, Review
from .forms import ReviewForm


class MovieDetail(DetailView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Movie.objects.filter(approved=True)
        movie = get_object_or_404(queryset, slug=slug)
        reviews = movie.reviews.order_by('-created_on')

        return render(
            request,
            "movies/movie_detail.html",
            {
                "movie": movie,
                "reviews": reviews,
                "review_form": ReviewForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Movie.objects.filter(approved=True)
        movie = get_object_or_404(queryset, slug=slug)
        reviews = movie.reviews.order_by('-created_on')

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.author = request.user
            review = review_form.save(commit=False)
            review.movie = movie
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "movies/movie_detail.html",
            {
                "movie": movie,
                "reviews": reviews,
                "review_form": ReviewForm(),
            },
        )


class UpdateReview(LoginRequiredMixin, UpdateView):
    model = Review

    fields = [
        "rating",
        "review_content",
    ]

    template_name = 'movies/update_review.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_name'] = self.object.movie

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
