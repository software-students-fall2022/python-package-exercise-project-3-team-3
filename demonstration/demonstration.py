from pyrecommendg3 import recommendations

def to_string(dictionary):
    string = ""
    for key in dictionary:
        string += str(key) + ": " + str(dictionary[key]) + "\n"
    return string

def main():
    print("--------------------------------------------")
    print("get_music_recommendation():")
    print()

    print("Suppose we want any music recommendation:")
    print(to_string(recommendations.get_music_recommendation()))

    print("Suppose we want a music recommendation of the Rock genre:")
    print(to_string(recommendations.get_music_recommendation(genre="Rock")))

    print("Suppose we want a music recommendation from Taylor Swift:")
    print(to_string(recommendations.get_music_recommendation(artist="Taylor Swift")))


    print("--------------------------------------------")


    print("get_food_recommendation():")
    print()

    print("Suppose we want any food recommendation:")
    print(to_string(recommendations.get_food_recommendation()))

    print("Suppose we want a food recommendation of the Thai cuisine:")
    print(to_string(recommendations.get_food_recommendation(cuisine='Thai')))

    print("Suppose we want a food recommendation of the Japanese cuisine without fish:")
    print(to_string(recommendations.get_food_recommendation(cuisine='Thai', allergen='Fish')))


    print("-------------------------------")


    print("get_movie_recommendation():")
    print()

    print("Suppose we want any movie recommendation:")
    print(to_string(recommendations.get_movie_recommendation()))
    
    print("Suppose we want a movie recommendation directed by James Cameron:")
    print(to_string(recommendations.get_movie_recommendation(director='James Cameron')))

    print("Suppose we want an action movie recommendation:")
    print(to_string(recommendations.get_movie_recommendation(genre='Action')))

    print("Suppose we want a movie recommendation rated PG-13:")
    print(to_string(recommendations.get_movie_recommendation(rating='PG-13')))

    print("Suppose we want a movie recommendation directed by James Cameron rated PG:")
    print(recommendations.get_movie_recommendation(director='James Cameron', rating='PG'))


    print("--------------------------------------------")


    print("view_all():")
    print()

    print("Suppose we want to view all music recommendations:")
    recommendations.view_all(category="Music")

    print()

    print("Suppose we want to view all movie recommendations:")
    recommendations.view_all(category="Movie")
    
    print()

    print('Suppose we want to view all food recommendations:')
    recommendations.view_all(category="Food")
  


if __name__ == '__main__':
    main()