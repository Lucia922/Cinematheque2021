from django import forms
from .models import Movie, MovieGenre, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
