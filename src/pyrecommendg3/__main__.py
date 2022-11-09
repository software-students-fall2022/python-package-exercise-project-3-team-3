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
    print()

    if answer == 5:
      break
    elif answer == 1:
      print(recommendations.get_music_recommendation())
    elif answer == 2:
      print(recommendations.get_movie_recommendation())
    elif answer == 3:
      print(recommendations.get_food_recommendation())
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