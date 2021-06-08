from django.shortcuts import render
from .models import MovieGenre, Movie, Review

# Create your views here.
def index(request):
    return render(request, 'cinema/index.html')

def movies(request):
    movie_list=Movie.objects.all()
    return render(request, 'cinema/movies.html', {'movie_list': movie_list})
    