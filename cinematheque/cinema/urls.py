from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('moviegenres/', views.moviegenres, name='moviegenres'),
    path('reviews/', views.reviews, name='reviews'),
    path('moviedetail/<int:id>', views.moviedetail, name='moviedetail'),
    path('reviewdetail/<int:id>', views.reviewdetail, name='reviewdetail'),
    path('newmovie/', views.newmovie, name='newmovie'),
    path('newreview/', views.newreview, name='newreview'),
]

