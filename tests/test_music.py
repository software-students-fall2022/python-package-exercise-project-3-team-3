import pytest

from pyrecommendg3 import recommendations

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

    def test_get_music_with_artist(self):
        """
        Test if get_music_recommendation() with a specified artist gets music only from that artist
        """
        test_artist = 'Pink Floyd'
        for i in range(10):
            actual = recommendations.get_music_recommendation(artist=test_artist).artist
            assert actual == test_artist, f"Expected the music returned by get_music_recommendation(artist='{test_artist}') to be from {test_artist}.  Instead, it returned from '{actual}'."