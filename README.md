[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9088947&assignment_repo_type=AssignmentRepo)

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
    Welcome to pypassgen - your simple and lightweight password generator!
    1. Generate a password
    2. Verify a password
    3. Encrypt a phrase
    4. Decrypt an encrypted phrase
    5. Exit
    Enter your choice (1 - 5):
    ```
