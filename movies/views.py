from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View, DetailView
from django.http import HttpResponse
from .models import Movie
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
