from django.contrib import admin
from .models import MovieGenre, Movie, Review
# Register your models here.
admin.site.register(MovieGenre)
admin.site.register(Movie)
admin.site.register(Review)
