from django.test import TestCase
from django.contrib.auth.models import User
from  .models import MovieGenre, Movie, Review
import datetime
from .forms import MovieForm
from .forms import ReviewForm
from django.urls import reverse_lazy, reverse

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

class NewMovieForm(TestCase):
    #valid form data
    def test_moviefrom(self):
        data={ 'moviename': "Band of Outsiders",
               'moviegenre': "Crime/Drama",
               'user': "Jinhee",
               'entrydate': "2021-6-08",
               'director': "Jean-Luc Godard",
               'Cast': "Jean-Luc Godard / Anna Karina / Sami Frey",
               'releasedate': "1966-3-15",
               'runtime': "1h 37m",
               'languages': "English / French",
               'about': "The film is an adaptation of the 1958 novel Fools' Gold by American author Dolores Hitchens."
             }

        form=MovieForm (data)
        self.assertTrue(form.is_valid)
   
    def test_movieform_Invalid(self):
        data={ 'moviename': "Band of Outsiders",
               'moviegenre': "Crime/Drama",
               'user': "Jinhee",
               'entrydate': "2021-06-08",
               'director': "Jean-Luc Godard",
               'Cast': "Jean-Luc Godard / Anna Karina / Sami Frey",
               'releasedate': "1966-03-15",
               'runtime': "1h 37m",
               'languages': "English / French",
               'about': "The film is an adaptation of the 1958 novel Fools' Gold by American author Dolores Hitchens."
             }
 
        form=MovieForm (data)
        self.assertTrue (form.is_valid)

class NewReviewForm(TestCase):
    #valid form data
    def test_reviewform(self):
        data={ 'reviewtitle': "A reverie of a gangster movie",
               'user': "Jinhee",
               'movie': "Band of Outsiders",
               'reviewdate': "2021-6-10",
               'reviewrating': "97",
               'reviewtext': "It’s as if a French poet took an ordinary banal American crime novel and told it to us in terms of the romance and beauty."
             }

        form=ReviewForm (data)
        self.assertTrue (form.is_valid)

    def test_reviewform_Invalid(self):
        data={ 'reviewtitle': "A reverie of a gangster movie",
               'user': "Jinhee",
               'movie': "Band of Outsiders",
               'reviewdate': "2021-06-10",
               'reviewrating': "97",
               'reviewtext': "It’s as if a French poet took an ordinary banal American crime novel and told it to us in terms of the romance and beauty."
             }

        form=ReviewForm (data)
        self.assertTrue (form.is_valid)

# Ran 10 tests OK
        
class New_Movie_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='zhopka#2016')
        self.genre=MovieGenre.objects.create(genrename='Comedy')
        self.movie=Movie.objects.create(moviename='Playtime', moviegenre=self.genre, user=self.test_user, 
                                        entrydate='2021-06-11', director='Jacqus Tati', 
                                        cast='Jean-Luc Godard / Anna Karina / Sami Frey',
                                        releasedate='1966-03-15', runtime='2h 4m', languages='French / English / German', 
                                        about="The film is an adaptation of the 1958 novel Fools' Gold by American author Dolores Hitchens.")
        
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmovie'))
        self.assertRedirects(response, '/accounts/login/?next=/cinema/newmovie/')

# Ran 11 tests Ok

class New_Review_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='zhopka#2016')
        self.genre=MovieGenre.objects.create(genrename='Comedy')
        self.movie=Movie.objects.create(moviename='Playtime', entrydate='2021-06-11', releasedate='1966-03-15',moviegenre=self.genre,
                                        user=self.test_user,)
        self.review=Review.objects.create(reviewtitle='French comedy masterpiece', user=self.test_user, movie=self.movie, reviewdate='2021-06-11',
                                          reviewrating='97',reviewtext='It happens to be one of those rare, supremely unique and utterly mind boggling examples of cinematic possibilities.')
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newreview'))
        self.assertRedirects(response, '/accounts/login/?next=/cinema/newreview/')

# Ran 12 tests OK, don't understand what this message means "django.db.utils.IntegrityError: null value in column "entrydate" of relation "movie" violates not-null constraint
#DETAIL:  Failing row contains (2, Playtime, null, 1966-03-15, , , 2, 2, null, null, null, )."

