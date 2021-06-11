from django.shortcuts import render, get_object_or_404
from .models import MovieGenre, Movie, Review
from .forms import MovieForm
from .forms import ReviewForm

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

def reviewdetail(request, id):
    review=get_object_or_404(Review, pk=id)
    return render(request, 'cinema/reviewdetail.html', {'review': review})

def newmovie(request):
    form=MovieForm
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MovieForm()
    else:
        form=MovieForm()
    return render(request, 'cinema/newmovie.html', {'form' : form})

def newreview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'cinema/newreview.html', {'form' : form})



    


