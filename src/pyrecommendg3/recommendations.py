import random

from .music_list import music_list
from .movie_list import movie_list

def __to_string(dictionary):
    string = ""
    for key in dictionary:
        string += key + ": " + dictionary[key] + "\n"
    return string

def get_music_recommendation(artist=None, genre=None):
    filtered_list = music_list
    if artist is not None:
        if type(artist) is not str:
            raise TypeError(f'Expected artist to be of type string, instead it was of type {type(artist)}')
        filtered_list = list(filter(lambda music: music['artist'].lower() == artist.lower(), filtered_list))

    if genre is not None:
        if type(genre) is not str:
            raise TypeError(f'Expected genre to be of type string, instead it was of type {type(genre)}')
        filtered_list = list(filter(lambda music: music['genre'].lower() == genre.lower(), filtered_list))
    
    if len(filtered_list) == 0:
        return f"No songs{' from artist '+ artist if artist else ''}{' of ' + genre + ' genre' if genre else ''} found.\n"

    song = random.choice(filtered_list)
    return song

def get_movie_recommendation(director=None, genre=None, rating=None):
    filtered_list = movie_list
    if director is not None:
        if type(director) is not str:
            raise TypeError(f'Expected director to be of type str, instead it was of type {type(director)}')
        filtered_list = list(filter(lambda movie: director == movie['director'], filtered_list))

    if genre is not None:
        if type(genre) is not str:
            raise TypeError(f'Expected genre to be of type string, instead it was of type {type(genre)}')
        filtered_list = list(filter(lambda movie: genre.lower() in movie['genre'], filtered_list))
        
    if rating is not None:
        if type(rating) is not str:
            raise TypeError(f'Expected rating to be of type string, instead it was of type {type(rating)}')   
        filtered_list = list(filter(lambda movie: rating.lower() == movie['rating'].lower(), filtered_list))
        
    if len(filtered_list) == 0:
        no_movies = (f"No movies{' directed by '+ director if director else ''}"
                    f"{' rated ' + rating if rating else ''}{' of ' + genre + ' genre' if genre else ''} found.\n")
        return no_movies

    movie = random.choice(filtered_list)
    return movie

def get():
    return "Success"
    