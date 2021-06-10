from django.contrib import admin
from .models import MovieGenre, Movie, Review
from embed_video.admin import AdminVideoMixin

# Register your models here.
admin.site.register(MovieGenre)
admin.site.register(Movie)
admin.site.register(Review)