from django.shortcuts import render, get_object_or_404
from .models import MovieGenre, Movie, Review

# Create your views here.
def index(request):
    return render(request, 'cinema/index.html')

def movies(request):
    movie_list=Movie.objects.all()
    return render(request, 'cinema/movies.html', {'movie_list': movie_list})

def moviedetail(request, id):
    movie=get_object_or_404(Movie, pk=id)
    return render(request, 'cinema/moviedetail.html', {'movie': movie})
    



def moviegenres(request):
    moviegenre_list=MovieGenre.objects.all()
    return render(request, 'cinema/moviegenres.html', {'moviegenre_list': moviegenre_list})

def reviews(request):
    review_list=Review.objects.all()
    return render(request, 'cinema/reviews.html', {'review_list': review_list})



