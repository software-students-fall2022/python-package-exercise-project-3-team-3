import random

from .music_list import music_list

def get_music_recommendation(author):
    filtered_list = music_list
    if author:
        filtered_list = filter(lambda music: music.author.lower() == author.lower(), filtered_list)

    return random.choice(filtered_list)

def get():
    return "Success"
    