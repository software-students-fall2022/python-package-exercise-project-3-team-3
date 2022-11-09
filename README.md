![Python build & test](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-3/actions/workflows/build.yaml/badge.svg)

# Python *`pyrecommendg3`* Package

Here's a package that gives you recommendations for different categories in music, movies, and food. 



## Team members
Pedro Baggio ([Jignifs](https://github.com/Jignifs))

Adam Sidibe ([Sidibee](https://github.com/sidibee))

Rachel Andoh ([rachel0lehcar](https://github.com/rachel0lehcar))

Manny Soto Ruiz ([MannySotoRuiz](https://github.com/MannySotoRuiz))

## Installation

- Create a `pipenv`-managed environment.

- Run the following command to install the lastest version of the package:

  ```bash
  pipenv install -i https://test.pypi.org/simple/ pypassgen==1.0.0
  ```

## Running package directly from the command line

- **_Initializing the package:_**

  - Run the following command in the terminal:

    ```python
    python -m pyrecommendg3
    ```

  - This will initialize the package and prompt the user to choose their desired function.

    ```bash
    Welcome to pyrecommendg3
    1. Get random music recommendation
    2. Get random movie recommendation
    3. Get random food recommendation
    4. View all recommendations
    5. Exit
    Enter your choice (1 - 5):
    ```

- **_Get music recommendation:_**

  - When prompted, enter `1` to get a random music recommendation.

  - User will be given a random music recommendation.

- **_Get movie recommendation:_**

  - When prompted, enter `2` to get a random movie recommendation.

  - User will be given a ranom movie recommendation

- **_Get food recommendation:_**

  - When prompted, enter `3` to get a random food recommendation.

  - User will be given a random food recommendation

- **_View all recommendations:_**

  - When prompted, enter `4` to view all recommendations menu.

  - Enter the category that you want to see.
  
  - User will be shown all recommendations for the category they want.

## Using the package as a module in a Python project

- Activate the virtual environment after installing the package:

  ```python
  pipenv shell
  ```

- Create a Python program that imports the package and its functions:

  ```python
  from pyrecommendg3 import recommendations
  ```

### Functions

- **_Get a music recommendation:_**

  - Call the `get_music_recommendation` function and pass the artist and genre to get a random music recommendation with those arguments. The function could also take no arguments to get a random music with any artisit and genre.
  
    | Parameters      | Description |
    | ------- | ------------- |
    | **artist : *str, default: None*** | Specifies the artist you want to get the music recommendation from. If not specified, will get from all artists.
    | **genre : *str, default: None***   | Specifies the genre of the recommended music. If not specified, will get from all genres.        |

    For example:

    ```python
    # in your project
    music = recommendations.get_music_recommendation()
    ```

- **_Get a movie recommendation:_**

  - Call the `get_movie_recommendation` function and pass the director, genre and rating to get a random movie recommendation with those arguments. The function could also take no arguments to get a random movie with any director, genre and rating.

    | Parameters      | Description |
    | ------- | ------------- |
    | **director : *str, default: None*** | Specifies the director you want to get the movie recommendation from. If not specified, will get from all movie directors.
    | **genre : *str, default: None***   | Specifies the genre of the recommended movie. If not specified, will get from all genres.        |
    | **rating : *str, default: None***   | Specifies the rating (PG, PG-13, etc.) of the recommended movie. If not specified, will get from all ratings.        |

    For example:

    ```python
    # in your project
    movie = recommendations.get_movie_recommendation()
    ```

- **_Get a food recommendation:_**

  - Call the `get_food_recommendation` function and pass the cuisine and allergen to get a random food recommendation with those arguments. The function could also take no arguments to get a random food with any cuisine and allergen.

    | Parameters      | Description |
    | ------- | ------------- |
    | **cuisine : *str, default: None*** | Specifies the cuisine of the recommended dish. If not specified, will get from all cuisines.
    | **allergen : *str, default: None***   | If specified, will only return dish recommendations without the specified allergen.      |

    For example:

    ```python
    # in your project
    food = recommendations.get_food_recommendation(cuisine='Japanese', allergen='Fish')
    ```

- **_View all recommendations:_**

  - Call the `view_all` function and pass a category string as argument

    | Parameters      | Description |
    | ------- | ------------- |
    | **category : *str, required*** | Specifies the category you want to view all recommendations from. Must be one of ['music', 'food', 'movie']|

    For example:

    ```python
    # in your project
    recommendations.view_all(category="Music")
    ```
## PyPI link to package
<https://test.pypi.org/project/pyrecommendg3/>