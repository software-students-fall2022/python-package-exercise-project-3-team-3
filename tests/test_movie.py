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
    def test_get_movie_with_genre(self):
        """
        Test if get_movie_recommendation() with specified genre gets movies only from that genre
        """
        test_genre = 'Fantasy'
        actual = recommendations.get_movie_recommendation(genre=test_genre)['genre']
        assert any(g.lower() == test_genre.lower() for g in actual), f"Expected the movie returned by get_movie_recommendation(genre='{test_genre}') to be from {test_genre} genre. Instead, it returned '{actual}'."
    
    def test_get_movie_with_director(self):
        """
        Test if get_movie_recommendation() with specified director gets movies only from that director
        """
        test_director = "James cameron"
        actual = recommendations.get_movie_recommendation(director=test_director)['director']
        assert actual.lower() == test_director.lower(), f"Expected the movie returned by get_movie_recommendation(director='{test_director}') to be directed by {test_director}. Instead, it returned '{actual}'."
    
    def test_get_movie_with_rating(self):
        """
        Test if get_movie_recommendation() with specified rating gets movies only with that rating
        """
        test_rating = 'Pg-13'
        actual = recommendations.get_movie_recommendation(rating=test_rating)['rating']
        assert actual.lower() == test_rating.lower(), f"Expected the movie returned by get_movie_recommendation(rating='{test_rating}') to be rated {test_rating}. Instead, it returned '{actual}'."

    # Not Found
    def test_get_movie_with_genre_not_found(self):
        test_genre = 'dystopian'
        actual = recommendations.get_movie_recommendation(genre=test_genre)
        assert actual == f'No movies of {test_genre} genre found.\n', f"Expected no movies of {test_genre} genre to be found, instead it returned: {actual}"

    def test_get_movie_with_director_not_found(self):
        test_director= "Foo Barstein"
        actual = recommendations.get_movie_recommendation(director=test_director)
        assert actual == f'No movies directed by {test_director} found.\n', f"Expected no movies directed by {test_director} to be found, instead it returned: {actual}"
    
    def test_get_movie_with_rating_not_found(self):
        test_rating = 'G'
        actual = recommendations.get_movie_recommendation(rating=test_rating)
        assert actual == f'No movies rated {test_rating} found.\n', f"Expected no movies rated {test_rating} to be found, instead it returned: {actual}"

    # Type Error
    def test_get_movie_with_wrong_director_parameter_types(self):
        """
        Test if get_movie_recommendation() with wrong director parameter type returns an error
        """
        with pytest.raises(TypeError):
            recommendations.get_movie_recommendation(director=3)

    def test_get_movie_with_wrong_genre_parameter_types(self):
        """
        Test if get_movie_recommendation() with wrong genre parameter type returns an error
        """
        with pytest.raises(TypeError):
            recommendations.get_movie_recommendation(genre=['test'])

    def test_get_movie_with_wrong_rating_parameter_types(self):
        """
        Test if get_movie_recommendation() with wrong rating parameter type returns an error
        """
        with pytest.raises(TypeError):
            recommendations.get_movie_recommendation(rating=3)

    # Combinations
    def test_get_movie_with_director_and_genre(self):
        """
        Test if get_movie_recommendation() with a specified director and genre gets movies only from that director and genre
        """
        test_director = "ChriS Columbus"
        test_genre = "Fantasy"
        for i in range(10):
            movie = recommendations.get_movie_recommendation(director=test_director, genre=test_genre)
            assert movie['director'].lower() == test_director.lower() and any(g.lower() == test_genre.lower() for g in movie['genre']), f"Expected the movie returned by get_movie_recommendation(director='{test_director}', genre='{test_genre}') to be from the {test_genre} genre and directed by {test_director}. Instead, it returned from '{movie['director']}' from the following genres '{movie['genre']}'."

    def test_get_movie_with_director_and_rating(self):
        """
        Test if get_movie_recommendation() with a specified director and rating gets movies only from that director and rating
        """
        test_director = "chris Columbus"
        test_rating = "Pg"
        for i in range(10):
            movie = recommendations.get_movie_recommendation(director=test_director, rating=test_rating)
            assert movie['director'].lower() == test_director.lower() and movie['rating'].lower() == test_rating.lower(), f"Expected the movie returned by get_movie_recommendation(director='{test_director}', rating='{test_rating}') to be rated {test_rating}  and directed by {test_director}. Instead, it returned from '{movie['rating']}' rated '{movie['director']}'."

    def test_get_movie_with_rating_and_genre(self):
        """
        Test if get_movie_recommendation() with a specified rating and genre gets movies only from that rating and genre
        """
        test_genre = "Fantasy"
        test_rating = "Pg"
        for i in range(10):
            movie = recommendations.get_movie_recommendation(genre=test_genre, rating=test_rating)
            assert movie['rating'].lower() == test_rating.lower() and any(g.lower() == test_genre.lower() for g in movie['genre']), f"Expected the movie returned by get_movie_recommendation(genre='{test_genre}', rating='{test_rating}') to be rated {test_rating}  and from the genre {test_genre}. Instead, it returned from '{movie['rating']}' from the following genres '{movie['genre']}'."

    # Combinations none found
    def test_get_movie_with_director_and_genre_not_found(self):
        """
        Test if get_movie_recommendation() with a genre and director combination not in the list returns an error message
        """
        test_director = "Foo Barstein"
        test_genre = "rock"
        actual = recommendations.get_movie_recommendation(director=test_director, genre=test_genre)
        assert actual == f'No movies directed by {test_director} of {test_genre} genre found.\n', f"Expected no movies directed by {test_director} of the {test_genre} genre to be found, instead it returned: {actual}"

    def test_get_movie_with_director_and_rating_not_found(self):
        """
        Test if get_movie_recommendation() with a rating and director combination not in the list returns an error message
        """
        test_rating = "G"
        test_director = "James Cameron"
        actual = recommendations.get_movie_recommendation(rating=test_rating, director=test_director)
        assert actual == f'No movies directed by {test_director} rated {test_rating} found.\n', f"Expected no movies rated {test_rating} directed by {test_director} to be found, instead it returned: {actual}"

    def test_get_movie_with_rating_and_genre_not_found(self):
        """
        Test if get_movie_recommendation() with a rating and genre combination not in the list returns an error message
        """
        test_rating = "PG"
        test_genre = "rock"
        actual = recommendations.get_movie_recommendation(rating=test_rating, genre=test_genre)
        assert actual == f'No movies rated {test_rating} of {test_genre} genre found.\n', f"Expected no movies rated {test_rating} of genre {test_genre} to be found, instead it returned: {actual}"
