import pytest

from pyrecommendg3 import recommendations
from pyrecommendg3.food_list import food_list

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
    
    def test_get_food(self):
        """
        Test if get_food_recommendation() returns a food in the list
        """
        for i in range(10):
            actual = recommendations.get_food_recommendation()
            assert actual in food_list, f"Expected the food returned by get_food_recommendation() to be in food_list. Instead, it returned '{actual}'."

    def test_get_food_with_cuisine(self):
        """
        Test if get_food_recommendation() with specified cuisine gets food only from that cuisine
        """
        test_cuisine = 'Japanese'
        actual = recommendations.get_food_recommendation(cuisine=test_cuisine)['cuisine']
        assert actual.lower() == test_cuisine.lower(), f"Expected the food returned by get_food_recommendation(cuisine='{test_cuisine}') to be of {test_cuisine} cuisine. Instead, it returned '{actual}'."

    def test_get_food_with_allergen(self):
        """
        Test if get_food_recommendation() with a specified allergen gets food without said allergen
        """
        test_allergen = 'Peanuts'
        for i in range(10):
            actual = recommendations.get_food_recommendation(allergen= test_allergen)['allergen']
            assert actual != test_allergen, f"Expected the food returned by get_food_recommendation(allergen='{test_allergen}') to be without the {test_allergen} allergen.  Instead, it returned with '{actual}'."

    def test_get_food_with_wrong_cuisine_parameter_types(self):
        """
        Test if get_food_recommendation() with wrong cuisine parameter type returns an error
        """
        with pytest.raises(TypeError):
            recommendations.get_food_recommendation(cuisine=3)

    def test_get_food_with_wrong_allergen_parameter_types(self):
        """
        Test if get_food_recommendation() with wrong allergen parameter type returns an error
        """
        with pytest.raises(TypeError):
            recommendations.get_food_recommendation(allergen=['test'])

    def test_get_food_with_cuisine_not_found(self):
        """
        Test if get_cuisine_recommendation() with a cuisine not in the list returns an error message
        """
        test_cuisine = 'Antartican'
        for i in range(10):
            actual = recommendations.get_music_recommendation(cuisine=test_cuisine)
            assert actual == f'No dish of {test_cuisine} cuisine found.\n', f"Expected no dish of the {test_cuisine} cuisine to be found, instead it returned: {actual}"

    def test_get_food_with_cuisine_and_allergen(self):
        """
        Test if get_food_recommendation() with a specified artist and genre gets music only from that artist and genre
        """
        test_cuisine = 'Japanese'
        test_allergen = 'Fish'
        for i in range(10):
            food = recommendations.get_music_recommendation(cuisine=test_cuisine, allergen=test_allergen)
            assert food['cuisine'] == test_cuisine and food['allergen'] != test_allergen, f"Expected the food returned by get_food_recommendation(cuisine='{test_cuisine}', allergen='{test_allergen}') to be from {test_cuisine} cuisine and without {test_allergen} allergen. Instead, it returned from '{food['cuisine']}' with the '{food['allergen']}' allergen."
