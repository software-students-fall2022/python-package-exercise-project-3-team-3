import pytest

from pyrecommendg3 import recommendations
from pyrecommendg3.music_list import music_list
from pyrecommendg3.movie_list import movie_list
from pyrecommendg3.food_list import food_list

class Tests:

    def test_view_all_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_view_all_with_wrong_category_type(self):
        """
        Test if view_all() with wrong artist parameter type returns an error
        """
        with pytest.raises(TypeError):
            recommendations.view_all(category=3)

    def test_view_all_with_wrong_category_entry(self):
        """
        Test if view_all() with the wrong category entry returns an error
        """
        test_category = "book"
        actual = recommendations.view_all(category=test_category)
        assert test_category != actual, f"Expected category to be music, movie or food, instead it was {test_category}"

    def test_view_all_with_category_music(self):
        """
        Test if view_all with music as the category prints all musics
        """
        test_category = "music"
        actual = recommendations.view_all(category=test_category)
        assert test_category == actual, f"Expected to view all {test_category}. Instead viewed all {actual}"
        

    def test_view_all_with_category_movie(self):
        """
        Test if view_all with music as the category prints all movies
        """
        test_category = "movie"
        actual = recommendations.view_all(category=test_category)
        assert test_category == actual, f"Expected to view all {test_category}. Instead viewed all {actual}"

    def test_view_all_with_category_food(self):
        """
        Test if view_all with music as the category prints all foods
        """
        test_category = "food"
        actual = recommendations.view_all(category=test_category)
        assert test_category == actual, f"Expected to view all {test_category}. Instead viewed all {actual}"