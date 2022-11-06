import random

from music_list import music_list

def __to_string(dictionary):
    string = ""
    for key in dictionary:
        string += key + ": " + dictionary[key] + "\n"
    return string
        


def get_music_recommendation(artist=None, genre=None):
    filtered_list = music_list
    if artist is not None:
        filtered_list = list(filter(lambda music: music['artist'].lower() == artist.lower(), filtered_list))

    if genre is not None:
        filtered_list = list(filter(lambda music: music['genre'].lower() == genre.lower(), filtered_list))
    
    if len(filtered_list) == 0:
        return f"No songs{' from artist '+ artist if artist else ''}{' of ' + genre + ' genre' if genre else ''} found.\n"

    return __to_string(random.choice(filtered_list))

def get():
    return "Success"
    