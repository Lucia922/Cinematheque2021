from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MovieGenre(models.Model):
    genrename=models.CharField(max_length=255)
    genredescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.genrename

    class Meta:
        db_table='moviegenre'
        verbose_name_plural='moviegenres'

class Movie(models.Model):
    moviename=models.CharField(max_length=255)
    moviegenre=models.ForeignKey(MovieGenre, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    entrydate=models.DateField()
    director=models.CharField(max_length=255, null=True, blank=True)
    cast=models.CharField(max_length=255, null=True, blank=True)
    releasedate=models.DateField()
    runtime=models.CharField(max_length=255)
    languages=models.CharField(max_length=255)
    about=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.moviename
    
    class Meta:
        db_table='movie'
        verbose_name_plural='movies'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table='review'
        verbose_name_plural='reviews'

    
    