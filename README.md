# Python Course Repository

This repository contains my coursework for the Python course. Each exercise is organized into separate folders for easy navigation.

## Folder Structure

- [Exercise 1.1: Getting Started with Python](#exercise-11-getting-started-with-python)
- [Exercise 1.2: Data Types in Python](#exercise-12-data-types-in-python)
- [Exercise 1.3: Operators & Functions in Python](#exercise-13-operators--functions-in-python)
- [Exercise 1.4: File Handling in Python](#exercise-14-file-handling-in-python)
- ...

## Getting Started

To access the exercises, simply navigate to the respective folders. Each folder contains the necessary files and instructions for completing the exercise.

## Exercise 1.1: Getting Started with Python

Install Python, check your version with python --version.

![Install Python](./add-python/install-python.png)

Create a new virtual environment named "cf-python-base", using the command **mkvirtualenv** cf-python-base
and then install iPython Shell to it with pip install ipython

![Create Virtual Environment](./add-python/cf-python-base.png)

Create a test with numbers and variables, having the user input numbers and print the result of them added together

![Adding Numbers](./add-python/adding.png)

Export a requirements file: 
1. Generate a requirements.txt file from source with **pip freeze > requirements.txt** command.  

2. Create  a new environment variable called cf-python-copy and then run the command **pip install -r requirements.txt**

## Exercise 1.2: Data Types in Python

Completed tasks 1-5 and added them to exercise 1.2 folder

Created each recipe individually using a Dictionary.  I chose a dictionary because it is easier 
to add multiple different data types and label each.

![Created Each Recipe in Dictionaries](./exercise1.2/create_recipes.png)

Created an all_recipes list to store each recipe dictionary.  I chose to use a list for all_recipes
since each recipe is the same data type and it's easier to go through a list.

![Created all_recipes list](./exercise1.2/create_all_recipes.png)

Added all the recipes to the "all_recipes" list and printed the all_recipes list.

![Add Recipes to all recipes](./exercise1.2/all_recipes_full.png)

Printed ingredients lists for all recipes.

![Printed List of All Ingredients](./exercise1.2/all_ingredients_list.png)
...
