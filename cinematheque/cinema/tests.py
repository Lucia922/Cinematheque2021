from django.test import TestCase
from django.contrib.auth.models import User
from  .models import MovieGenre, Movie, Review
import datetime

# Create your tests here.
class MovieGenreTest(TestCase):
    def setUp(self):
        self.genre=MovieGenre(genrename='Comedy', genredescription='A comedy film is a category of film in which the main emphasis is on humor. These films are designed to make the audience laugh through amusement and most often work by exaggerating characteristics for humorous effect. Films in this style traditionally have a happy ending (black comedy being an exception).')

    def test_genrestring(self):
        self.assertEqual(str(self.genre), 'Comedy', 'A comedy film is a category of film in which the main emphasis is on humor. These films are designed to make the audience laugh through amusement and most often work by exaggerating characteristics for humorous effect. Films in this style traditionally have a happy ending (black comedy being an exception).' )

    
    def test_tablename(self):
        self.assertEqual(str(MovieGenre._meta.db_table), 'moviegenre')

class MovieTest(TestCase):
    def setUp(self):
        self.genre=MovieGenre(genrename='Comedy')
        self.moviename=Movie(moviename='Playtime')
        self.user=User(username='Jinhee')
        self.entrydate=Movie(entrydate=datetime.date(2021,6,11))
        self.director=Movie(director='Jacques Tati')
        self.runtime=Movie(runtime='2h 4m')
        self.languages=Movie(languages='French / English / German')
        
    def test_moviestring(self):
            self.assertEqual(str(self.moviename), 'Playtime')

    def test_tablename(self):
            self.assertEqual(str(Movie._meta.db_table), 'movie')

class ReviewTest(TestCase):
    def setUp(self):
        self.title=Review(reviewtitle='French comedy masterpiece')
        self.user=User(username='Jinhee')
        self.moviename=Movie(moviename='Playtime')
        self.reviewdate=Review(reviewdate=datetime.date(2021,6,11))
        self.rating=Review(reviewrating='97')
        self.text=Review(reviewtext='It happens to be one of those rare, supremely unique and utterly mind boggling examples of cinematic possibilities.')

    def test_reviewstring(self):
        self.assertEqual(str(self.title), 'French comedy masterpiece')

    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'review')

#Ran 6 tests OK




