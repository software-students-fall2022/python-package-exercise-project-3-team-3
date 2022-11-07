import pytest

from pyrecommendg3 import recommendations
from pyrecommendg3.music_list import music_list

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

    
    def test_get_music(self):
        """
        Test if get_music_recommendation() returns a song in the list
        """
        for i in range(10):
            actual = recommendations.get_music_recommendation()
            assert actual in music_list, f"Expected the music returned by get_music_recommendation() to be in music_list.  Instead, it returned '{actual}'."

    def test_get_music_with_wrong_artist_parameter_types(self):
        """
        Test if get_music_recommendation() with wrong artist parameter type returns an error
        """
        with pytest.raises(TypeError):
            recommendations.get_music_recommendation(artist=3)

    def test_get_music_with_wrong_genre_parameter_types(self):
        """
        Test if get_music_recommendation() with wrong genre parameter type returns an error
        """
        with pytest.raises(TypeError):
            recommendations.get_music_recommendation(genre=['test'])

    def test_get_music_with_artist(self):
        """
        Test if get_music_recommendation() with a specified artist gets music only from that artist
        """
        test_artist = 'Pink Floyd'
        for i in range(10):
            actual = recommendations.get_music_recommendation(artist=test_artist)['artist']
            assert actual == test_artist, f"Expected the music returned by get_music_recommendation(artist='{test_artist}') to be from {test_artist}.  Instead, it returned from '{actual}'."

    def test_get_music_with_artist_not_found(self):
        """
        Test if get_music_recommendation() with an artist not in the list returns an error message
        """
        test_artist = 'Foo Barstein'
        actual = recommendations.get_music_recommendation(artist=test_artist)
        assert actual == f'No songs from artist {test_artist} found.\n', f"Expected no songs from artist {test_artist} to be found, instead it returned: {actual}"

    def test_get_music_with_genre(self):
        """
        Test if get_music_recommendation() with a specified genre gets music only from that genre
        """
        test_genre = 'Rock'
        for i in range(10):
            actual = recommendations.get_music_recommendation(genre=test_genre)['genre']
            assert actual == test_genre, f"Expected the music returned by get_music_recommendation(genre='{test_genre}') to be from the {test_genre} genre.  Instead, it returned from '{actual}'."

    def test_get_music_with_genre_not_found(self):
        """
        Test if get_music_recommendation() with a genre not in the list returns an error message
        """
        test_genre = 'Cars'
        for i in range(10):
            actual = recommendations.get_music_recommendation(genre=test_genre)
            assert actual == f'No songs of {test_genre} genre found.\n', f"Expected no songs of the {test_genre} genre to be found, instead it returned: {actual}"

    def test_get_music_with_artist_and_genre(self):
        """
        Test if get_music_recommendation() with a specified artist and genre gets music only from that artist and genre
        """
        test_genre = 'Rock'
        test_artist = "Guns N' Roses"
        for i in range(10):
            song = recommendations.get_music_recommendation(artist=test_artist, genre=test_genre)
            assert song['artist'] == test_artist and song['genre'] == test_genre, f"Expected the music returned by get_music_recommendation(artist='{test_artist}', genre='{test_genre}') to be from the {test_genre} genre and the {test_artist} artist. Instead, it returned from '{song['artist']}' from the '{song['genre']}' genre."

    def test_get_music_with_artist_and_genre_not_found(self):
        """
        Test if get_music_recommendation() with a genre and artist combination not in the list returns an error message
        """
        test_genre = 'Pop'
        test_artist = "Pink Floyd"
        actual = recommendations.get_music_recommendation(artist=test_artist, genre=test_genre)
        assert actual == f'No songs from artist {test_artist} of {test_genre} genre found.\n', f"Expected no songs from {test_artist} of the {test_genre} genre to be found, instead it returned: {actual}"