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

    def test_get_music_with_author(self):
        """
        Test if get_music_recommendation() with a specified author gets music only from that author
        """
        test_author = 'Pink Floyd'
        for i in range(10):
            actual = recommendations.get_music_recommendation(author=test_author).author
            assert actual == test_author, f"Expected the music returned by get_music_recommendation(author='{test_author}') to be from {test_author}.  Instead, it returned from '{actual}'."