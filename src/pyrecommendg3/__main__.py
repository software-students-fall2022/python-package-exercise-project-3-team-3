from pyrecommendg3 import recommendations

def main():
  print(recommendations.get_music_recommendation(artist="Taylor Swift"))
  print(recommendations.get_music_recommendation(genre="Rock"))
  print(recommendations.get_music_recommendation())
  print()
  recommendations.view_all(category="Music")
  print()
  recommendations.view_all(category="Movie")
  print()
  recommendations.view_all(category="Food")
  


if __name__ == '__main__':
    main()