from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from .models import Movie, Review
from .forms import ReviewForm, AddMovieForm, UpdateMovieForm


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


class DeleteReview(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'movies/delete_review.html'
    success_url = reverse_lazy('home')


class AddMovie(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = AddMovieForm
    template_name = 'movies/add_movie.html'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['name'] = 'Enter Movie Name'
        initial['director'] = 'Enter Movie Director'
        initial['summary'] = 'Enter a summary for the movie. NO SPOILERS!'
        return initial

    def post(self, request):
        if request.method == "POST":
            form = AddMovieForm(request.POST)
            if form.is_valid():
                new_movie = form.save(commit=False)
                new_movie.slug = slugify(new_movie.name)
                new_movie.save()
        form = AddMovieForm()
        return redirect("home")


class UpdateMovie(UserPassesTestMixin, UpdateView):
    model = Movie
    form_class = UpdateMovieForm
    template_name = 'movies/update_movie.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser
