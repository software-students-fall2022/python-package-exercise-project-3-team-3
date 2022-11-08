import pytest

from pyrecommendg3 import recommendations
from pyrecommendg3.movie_list import movie_list

class Tests:

    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    # Works with no Parameters
    def test_get_movie(self):
        """
        Test if get_movie_recommendation() returns a movie in the list
        """
        for i in range(10):
            actual = recommendations.get_movie_recommendation()
            assert actual in movie_list, f"Expected the movie returned by get_movie_recommendation() to be in movie_list. Instead, it returned '{actual}'."

    # Works with Parameters 
    def test_get_movie_with_director(self):
        """
        Test if get_movie_recommendation() with specified director gets movies only from that director
        """
        test_director = 'James Cameron'
        actual = recommendations.get_movie_recommendation(director=test_director)['director']
        assert actual.lower() == test_director.lower(), f"Expected the movie returned by get_movie_recommendation(director='{test_director}') to be a movie directer by {test_director}. Instead, it returned '{actual}'."
    
    def test_get_movie_with_actor(self):
        """
        Test if get_movie_recommendation() with specified actor gets movies only starring that actor
        """
        test_actor = 'Leonardo DiCaprio'
        actual = recommendations.get_movie_recommendation(leading_actor=test_actor)['leading_actor']
        assert any(a.lower() == test_actor.lower() for a in actual), f"Expected the movie returned by get_movie_recommendation(leading_actor='{test_actor}') to be a movie starring {test_actor}. Instead, it returned '{actual}'."

    def test_get_movie_with_genre(self):
        """
        Test if get_movie_recommendation() with specified genre gets movies only from that genre
        """
        test_genre = 'fantasy'
        actual = recommendations.get_movie_recommendation(genre=test_genre)['genre']
        assert any(g.lower() == test_genre.lower() for g in actual), f"Expected the movie returned by get_movie_recommendation(genre='{test_genre}') to be from {test_genre} genre. Instead, it returned '{actual}'."
    
    def test_get_movie_with_year(self):
        """
        Test if get_movie_recommendation() with specified year gets movies only from that year
        """
        test_year = 2001
        actual = recommendations.get_movie_recommendation(year=test_year)['year']
        assert actual == test_year, f"Expected the movie returned by get_movie_recommendation(genre='{test_year}') to be from the year{test_year}. Instead, it returned '{actual}'."
    
    def test_get_movie_with_rating(self):
        """
        Test if get_movie_recommendation() with specified rating gets movies only with that rating
        """
        test_rating = 'PG-13'
        actual = recommendations.get_movie_recommendation(rating=test_rating)['rating']
        assert actual == test_rating, f"Expected the movie returned by get_movie_recommendation(rating='{test_rating}') to be rated {test_rating}. Instead, it returned '{actual}'."
