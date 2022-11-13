from pyrecommendg3 import recommendations

def main():

  print("Welcome to the pyrecommendg3")
  while (True):
    print("1. Get random music recommendation")
    print("2. Get random movie recommendation")
    print("3. Get random food recommendation")
    print("4. View all recommendations")
    print("5. Exit")

    answer = int(input("Enter your choice (1-5): "))
    

    if answer == 5:
      break
    elif answer == 1:
      artist = input("Enter artist (leave empty if you want from any artist): ")
      genre = input("Enter genre (leave empty if you want from any genre): ")
      if artist == "":
        artist = None
      if genre == "":
        genre = None
      print(recommendations.get_music_recommendation(artist=artist, genre=genre))
    elif answer == 2:
      director = input("Enter director (leave empty if you want from any director): ")
      genre = input("Enter genre (leave empty if you want from any genre): ")
      rating = input("Enter rating (PG-13, PG, etc.) (leave empty if you want from any rating): ")
      if director == "":
        director = None
      if genre == "":
        genre = None
      if rating == "":
        rating = None
      print(recommendations.get_movie_recommendation(director=director, genre=genre, rating=rating))
    elif answer == 3:
      cuisine = input("Enter cuisine (leave empty if you want from any cuisine): ")
      allergen = input("Enter allergen (leave empty if you don't want to consider allergens): ")
      if cuisine == "":
        cuisine = None
      if allergen == "":
        allergen = None
      print(recommendations.get_food_recommendation(cuisine=cuisine, allergen=allergen))
    elif answer == 4:
      print("1. View all music")
      print("2. View all movies")
      print("3. View all foods")
      choice = int(input("Enter your choice (1-3): "))
      if choice == 1:
        recommendations.view_all(category="Music")
      elif choice == 2:
        recommendations.view_all(category="Movie")
      elif choice == 3:
        recommendations.view_all(category="Food")
      else:
        print("Incorrect input")
    else:
      print("Incorrect input. Please try again")
    print()
    print()

if __name__ == '__main__':
    main()