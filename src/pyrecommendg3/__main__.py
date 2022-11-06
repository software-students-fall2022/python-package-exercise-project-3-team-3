import recommendations

def main():
  print(recommendations.get_music_recommendation(artist="Taylor Swift"))
  print(recommendations.get_music_recommendation(genre="Rock"))
  print(recommendations.get_music_recommendation())
  


if __name__ == '__main__':
    main()