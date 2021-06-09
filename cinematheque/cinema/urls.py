from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('moviegenres/', views.moviegenres, name='moviegenres'),
    path('reviews/', views.reviews, name='reviews'),
    path('moviedetail/<int:id>', views.moviedetail, name='detail'),
]

