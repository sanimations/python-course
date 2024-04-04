# Python Course Repository

This repository contains my coursework for the Python course. Each exercise is organized into separate folders for easy navigation.

## Folder Structure

- [Exercise 1.1: Getting Started with Python](#exercise-11-getting-started-with-python)
- [Exercise 1.2: Data Types in Python](#exercise-12-data-types-in-python)
- [Exercise 1.3: Operators & Functions in Python](#exercise-13-operators--functions-in-python)
- [Exercise 1.4: File Handling in Python](#exercise-14-file-handling-in-python)
- [Exercise 1.5: Object-Oriented Programming in Python](#exercise-15-object--oriented-programming-in-python)
- [Exercise 1.6: Databases in Python](#exercise-16-databases-in-python)
- [Exercise 1.7: Object-Relational Mapping in Python](#exercise-17-object--relational-mapping-in-python)

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

2. Create a new environment variable called cf-python-copy and then run the command **pip install -r requirements.txt**

## Exercise 1.2: Data Types in Python

Completed tasks 1-5 and added them to exercise 1.2 folder

Created each recipe individually using a Dictionary. I chose a dictionary because it is easier
to add multiple different data types and label each.

![Created Each Recipe in Dictionaries](./exercise1.2/create_recipes.png)

Created an all_recipes list to store each recipe dictionary. I chose to use a list for all_recipes
since each recipe is the same data type and it's easier to go through a list.

![Created all_recipes list](./exercise1.2/create_all_recipes.png)

Added all the recipes to the "all_recipes" list and printed the all_recipes list.

![Add Recipes to all recipes](./exercise1.2/all_recipes_full.png)

Printed ingredients lists for all recipes.

![Printed List of All Ingredients](./exercise1.2/all_ingredients_list.png)

## Exercise 1.3: Operators & Functions in Python

Initialize the global variables for both the recipe book and all the ingredients

![Create Global Variables](./exercise1.3/global_variables_01.png)

Create a function to get the recipe from the user. Get user input for the Name of the recipe, the time it took to cook and each of the ingredients.

Use .split(',') in the ingredients input to allow the user to separate each ingredient or use a while loop with a "STOP" input to break when the user enters "STOP".

Then create and return a dictionary "recipe" of the name, cooking time, and ingredients list.

![Create Function to Get Recipes from User Input](./exercise1.3/take_recipe_function_02.png)

Ask user to input amount of recipes, then loop through each of the recipes, adding them to the recipes_list and any new ingredients to the ingredients_list.

The first for loop repeats for the amount of recipes the user input, n, and initializes a new recipe by using the take_recipe() function which we already created. Then it appends the current recipe to the recipes_list.

The second for loop looks at each ingredient in the current recipe and checks if the ingredients_list does **not** contain the ingredient already. If not, the ingredient is added to the list.

![User Inputs # of Recipes and loop through each to add to recipes_list and ingredients_list](./exercise1.3/quantity_for_take_recipe_03.png)

Create difficulty rating for each recipe. Create conditionals for if the recipe is above or below 10 minutes cooking time and/or if the recipe contains above or below 4 ingredients. Then append to the reciples list by adding the new key-value pair to the dictionaries with ```recipe['difficulty'] = difficulty```.

![Generate For Loop to Calculate Difficulty Rating](./exercise1.3/difficulty_04.png)

Print out each recipe with the name, cooking time, ingredients, and difficulty. Iterate through each ingredient to have them print on individual lines.

![Print Each Recipe With Difficulty Rating](./exercise1.3/all_recipes_05.png)

Print all the ingredients needed to make all the recipes by printing the ingredients_list.  Again, iterating through each ingredient in a for loop so they print on their own line.

![Print Each Recipe With Difficulty Rating](./exercise1.3/all_ingredients_06.png)

Go into powershell/command prompt and go into the folder with Exercise1.3.  Then turn on the virtual environment and run ```python Exercise_1.3.py```.  Follow the prompts to see your next grocery list!

![Example of Exercise1.3 running in Powershell](./exercise1.3/powershell_final_example.png)

## Exercise 1.4: File Handling in Python

### Part 1: Create recipe_input.py Script

1. **Importing pickle module**
   - Begin by importing the `pickle` module to work with binary files.

2. **Define take recipe function:**
    - Define a function `take_recipe()` to collect recipe details from the user. This function will:
        - Prompt the user for the recipe name, cooking time, and ingredients.
        - Calculate the difficulty of the recipe using the `calc_difficulty()` function.
        - Return a dictionary containing the recipe details.

3. **Calculating recipe difficulty:**
   - Define the function `calc_difficulty()` to determine the difficulty level of a recipe based on certain criteria:
     - If cooking time is less than 10 minutes and ingredients are fewer than 4, set difficulty to Easy.
     - If cooking time is less than 10 minutes and ingredients are 4 or more, set difficulty to Medium.
     - If cooking time is 10 minutes or more and ingredients are fewer than 4, set difficulty to Intermediate.
     - If cooking time is 10 minutes or more and ingredients are 4 or more, set difficulty to Hard.

**BE WARNED** The order of the code matters, a function cannot be called before it is written, so `calc_difficulty()` must be placed before `take_recipe()` since it will be called within `take_recipe()`.  

![Importing pickle and creating two functions](./exercise1.4/part1_steps1-3.png)

4. **Handling file input/output:**
   - Prompt the user to input a filename for the binary file where recipe data will be stored.
   - Utilize a try-except block to handle file operations:
     - Attempt to open the specified file in read mode (`'rb'`).
     - If the file is not found, create a new dictionary `data` containing `recipes_list` and `all_ingredients`.
     - Close the file stream in the else block.
     - Finally, extract the values from the dictionary into separate lists (`recipes_list` and `all_ingredients`).

![Filename and try-except block for saving data](./exercise1.4/part1_step4.png)

5. **Entering multiple recipes:**
   - Ask the user how many recipes they want to enter.
   - Utilize a for loop to iterate through the specified number of recipes.
   - Within the loop, call the `take_recipe()` function to gather recipe details and append them to the `recipes_list`.
   - Parse through each recipe's ingredients and add unique ingredients to the `all_ingredients` list.

![Ask for number of recipes to loop through and save recipe data](./exercise1.4/part1_step5.png)

6. **Gathering recipe data:**
   - After gathering all recipe details, assemble the updated `recipes_list` and `all_ingredients` into a dictionary named `data`.
   - This dictionary contains two keys: `recipes_list` and `all_ingredients`, each corresponding to their respective lists.

7. **Saving data to a binary file:**
   - Utilize a try-except block to handle file input/output operations for saving data.
   - Open the specified binary file in write mode (`'wb'`).
   - Utilize the `pickle.dump()` function to write the `data` dictionary to the binary file.
   - Display a success message upon successful data save.
   - Include error handling to catch any exceptions that may occur during the file save operation.

![Gather recipe data and save to a binary file](./exercise1.4/part1_step6-7.png)

### Part 2: Create recipe_search.py Script

1. **Importing the pickle module:**
   - Ensure that the script begins with importing the pickle module to enable working with binary files.

2. **Defining the display_recipe() function:**
   - Define a function called `display_recipe(recipe : dict)` that takes a recipe dictionary as an argument.
   - Within this function, print all attributes of the recipe including its name, cooking time, ingredients, and difficulty.

   ![Import pickle and create display_recipe() function](./exercise1.4/part2_steps1-2.png)

3. **Defining the search_ingredient() function:**
   - Define a function called `search_ingredient(data : dict)` that takes a data dictionary as an argument.
   - The function should first display all available ingredients from the data dictionary under the key `all_ingredients`.
   - Each ingredient should be displayed with a number using the `enumerate()` function.
   - Then, implement a try block where the user selects a number corresponding to an ingredient from the list.
   - Store the selected ingredient into a variable called `ingredient_searched`.
   - Add an except clause to handle incorrect user inputs.
   - Finally, add an else clause to iterate through every recipe in the data dictionary (using the key `recipes_list`).
   - For each recipe, check if the `ingredient_searched` is in the recipe's ingredients list. If found, print the recipe's name.

![Create search_ingredient() function with try-except blocks](./exercise1.4/part2_step3.png)

4. **Asking for the filename:**
   - Prompt the user to enter the name of the file containing the recipe data.

5. **Opening and extracting data from the file:**
   - Use a try block to open the file specified by the user using the pickle module.
   - Extract the contents of the file into a variable called `data`.

6. **Handling file not found:**
   - Add an except block to handle the FileNotFoundError in case the specified file is not found.
   - Display a warning message to the user indicating that the file hasn't been found.

7. **Calling the search_ingredient() function:**
   - Define an else block that is executed when the file is successfully opened and its contents are extracted.
   - Call the `search_ingredient()` function, passing the `data` dictionary as an argument.

   ![Create search_ingredient() function with try-except blocks](./exercise1.4/part2_steps4-7.png)

   ## Exercise 1.5: Object-Oriented Programming in Python

### Part 1. Define Recipe Class

1. Define a class named `Recipe`.
2. Define the following data attributes:
    1. `name`: Name of the recipe.
    2. `ingredients`: List of ingredients.
    3. `cooking_time`: Time taken in minutes to carry out the recipe.
    4. `difficulty`: Auto-generated attribute indicating the difficulty level.

   ![Created Recipe Class and added init method](./exercise1.5/part1.png)

### Part 2. Create Methods

1. Initialization method to set up recipe attributes.
2. Getter and setter methods for `name` and `cooking_time`.

   ![Created getters and setters for name and cooking time](./exercise1.5/getters_setters.png)

3. Method to calculate and get difficulty.

   ![Created a method to calculate difficulty](./exercise1.5/calc_diff_method.png)

4. Method to add ingredients, search ingredients, get ingredients, and update all ingredients.

   ![Created methods for the ingredients list within the recipe](./exercise1.5/add_get_search_update_ingredients.png)

5. Method to search for recipes by a specified ingredient.

   ![Created a method to find all recipes with specific ingredient](./exercise1.5/recipe_search.png)

6. Method to print recipe as a string.

   ![Method for printing recipes as string](./exercise1.5/string_recipe.png)


### Part 3: Working with Recipe Objects

1. Instantiate objects for Tea, Coffee, Cake, and Banana Smoothie.

2. Create a list called `recipes_list` with all recipe objects.

3. Use the `recipe_search()` method to find recipes containing specific ingredients.

   ![Recipe Object tests](./exercise1.5/test_class_methods.png)

**OUTPUT**


   ![Recipe Object test results](./exercise1.5/recipe_oop_printed.png)

   ## Exercise 1.6: Databases in Python

### Part 1: Create & Connect Database

1. Import the ```mysql.connector``` module and initialize the object ```conn``` to connect the parameters setup in MySQL.
   This includes:
      - Hostname = `localhost`
      - Username = `cf-python`
      - Password = `password`

2. Initialize a ```cursor``` object from the ```conn```, then create a database called ```task_database```.
- Use EXISTS when creating the database to avoid making duplicates of the same name:
   ```python
   cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
   ```

- Make sure to USE the correct database
   ```python
   cursor.execute("USE task_database")
   ```

3. Create a table called ```Recipes``` with the columns:
   - id
   - name
   - ingredients
   - cooking_time
   - difficulty

   All look familiar to previous tasks, except for id which will use ```INT PRIMARY KEY AUTO_INCREMENT``` to automatically increment its value

### Part 2: Create the Main Menu

1. Create a `main_menu(conn,cursor)` function that takes conn and cursor arguments.  Making sure to end your code with:
```python
if __name__ == "__main__":
    main_menu(conn, cursor)
```
Doing this will ensure the main_menu method runs first.

2. Inside the main_menu method, create a while loop that goes through multiple choices, only exiting the loop when the user types 'done'.

3. Ask the user to make a choice and make the 4 choices:
- `create_recipe(cursor)` to create a new recipe 
- `search_recipe(cursor)` to search for a recipe by ingredient 
- `update_recipe(cursor)` to update a current recipe 
- `delete_recipe(cursor)` to remove a recipe from the Recipes table 


4. Outside of the choices add `conn.commit` to commit any changes made after each method is complete. And outside of the loop add `cursor.close()` and `conn.close()` to exit the database after committing. 

### Part 3: Creating a Recipe with create_recipe(cursor)

Collect the data from the user and calculate the difficulty with calc_difficulty() method.

```python
   new_recipe = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
   val = (r_name, r_ingredients, r_cooking_time, r_difficulty)
   cursor.execute(new_recipe, val)
```

   ![Create Recipe](./exercise1.6/create_recipe.png)

In the image, the recipe for ravioli is being created!

### Part 4: Searching for a Recipe with search_recipe(cursor)

Create a list of all the ingredients in all recipes, without any duplicates. Create a list and then loop through it allowing for an index column. Then search through all Recipes ingredients to show the user each recipe that contains the specified ingredient.

```python
   query = "SELECT * FROM Recipes WHERE LOWER(ingredients) LIKE %s"
    cursor.execute(query, ("%" + search_ingredient + "%",))
```

   ![Search by Ingredient](./exercise1.6/search_by_ingredient.png)


### Part 5: Updating a Recipe with update_recipe()

Prompt user to choose a recipe to update by typing the recipe name from a list of each recipe. Then prompt the user for which section to update. Finally, ask what new value is desired.  Make sure to change cooking_time to an int if that is what changed.  Then update the recipe in the Recipes table:

```python
update_query = f"UPDATE Recipes SET {update_key} = %s WHERE name = %s"
cursor.execute(update_query, (update_value, update_name))
```

   ![Update Recipe](./exercise1.6/update_recipe_1.png)

**BUT WAIT**
Check if the section being changed is cooking_time or ingredients because then the difficulty will need to be checked. Add two if statements checking for cooking_time or ingredients. Whichever is input, search the table for the other to run the calc_difficulty method.  Finally, UPDATE the new difficulty.

   ![Updated Difficulty](./exercise1.6/update_ravioli.png)

In the first image, ravioli had 4 ingredients and was labeled 'Hard', but after removing an ingredient the difficulty changed to 'Intermediate'

### Part 6: Deleting a Recipe with delete_recipe()

Prompt the user for the name of the recipe to be deleted. Use the DELETE statement to search the Recipes table and remove the one with the matching name:

```python
   delete_rec = input("Please enter recipe name you wish to remove: ")
   cursor.execute("DELETE FROM Recipes WHERE name = %s", (delete_rec,))
```

   ![Delete Recipe](./exercise1.6/delete_recipe.png)


   ## Exercise 1.7: Object-Relational Mapping in Python

### Part 1: Set Up Your Script & SQLAlchemy

1. Create a new script file and add all the necessary imports:

```python
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
```

2. Make sure MySQL Server is up.  Use the credentials found to create an engine object called `engine` that connects to the desired database.  Then generate the Session class, bind it to the engine, and initialize the session object.

```python
engine = create_engine("mysql://cf-python:password@localhost/task_database")
Session = sessionmaker(bind=engine)
session = Session()
```

### Part 2: Create Your Model and Table

1. Store the declarative base class into a variable called `Base`.  Create the Recipe model with the Recipe class inheriting the Base class.  Also, set the `__tablename__ = 'final_recipes'`

2. The table should be made of an id, name, ingredients, cooking_time, and difficulty column, the same as exercise 1.6.  A visual of the table is shown below:

| Field        | Type         | Null | Key | Default | Extra          |
|--------------|--------------|------|-----|---------|----------------|
| id           | int          | NO   | PRI | NULL    | auto_increment |
| name         | varchar(50)  | YES  |     | NULL    |                |
| ingredients  | varchar(255) | YES  |     | NULL    |                |
| cooking_time | int          | YES  |     | NULL    |                |
| difficulty   | varchar(20)  | YES  |     | NULL    |                |


3. Define a `__repr__` method that shows the recipe id, name, and difficulty.

4. Define a `__str__` method that will be shown anytime the recipe is printed. Add all the information of the recipe and make sure it is shown nicely. Be creative.

5. Define a method called `calc_difficulty` which will calculate how difficult a recipe is when called.

6. Once complete, create the corresponding table on the database with `Base.metadata.create_all(engine)`

### Part 3: Define your Main Operations as Functions

1. `create_recipe()`
- Collect the details for the recipe name and cooking time
- Check the inputs are all appropriate
- Collect the ingredients from the user by asking how many ingredients they would like to enter and then adding each ingredient to a list
- Convert the ingredients list into a string
- Generate the recipe difficulty with `calc_difficulty()`
- Add the recipe with `session.add(new_recipe)` and then committing the recipe to the session

   ![Create Recipe](./exercise1.7/create_ravioli.png)

2. `view_all_recipes()`
- Check if there are any recipes, if not then tell the user to add more before trying again
- Retrieve all Recipes and loop through them calling each of their `__str__` methods by printing them

   ![view All Recipes](./exercise1.7/view_all_recipes.png)

3. `search_by_ingredients`
- Check with `count()` method if there are any recipes, if not then tell the user to add more before trying again
- Create a list of all the ingredients, no duplicates, each with a number next to them
- Let the user choose any number of ingredients, check to make sure the numbers are on the list
- Make a new list of ingredients filled with what the user wants to search by
- Create a conditions list and then loop through the ingredients in the recipes see if all the searched ingredients are met using like_term string
- Finally, `filter()` through the query with the recipes containing the conditions and display them using the `__str__` method

### Example of searching by one ingredient:
   ![search by one ingredient](./exercise1.7/search_by_one_ingredient.png)

### Example of searching by multiple ingredients:

   ![search by multiple ingredients](./exercise1.7/search_by_multiple_ingredients.png)

4. `edit_recipe()`
- Check with `count()` method if there are any recipes, if not then tell the user to add more before trying again
- Show the user all the recipes with the `__repr__` method because they only need the name and ID for now
- Display the chosen recipe, then let the user pick a recipe by ID and prompt them to type '1', '2', or '3' depending on what they want to change
- Create if-else statements based on what they chose to change, checking to make sure that the newly input changes are valid
- If cooking time or ingredients are changed then difficulty will also need to be updated
- Commit the changes with `session.commit()`

   ![Update Milkshake](./exercise1.7/update_milkshake.png)

5. `delete_recipe()`
- Check with `count()` method if there are any recipes, if not then tell the user to add more before trying again
- Show the user all the recipes with the `__repr__` method
- Prompt the user to type the recipe ID of the recipe they would like removed, then make sure it is a valid ID
- Ask the user if they are sure they would like to delete the recipe, if prompted YES then remove it with `session.delete(recipe)`

   ![Remove Stew](./exercise1.7/remove_stew.png)

### Example from MySQL showing the updated Milkshakes and removed Stew
   ![Final Recipes in MySQL](./exercise1.7/mySQL_final_recipes.png)

   ### Part 4: Design Your Main Menu

Same as exercise 1.6. Create a `while` loop that will break once the user types 'quit'  Except in this one don't use conn or cursor and instead use `session.commit()`, `session.close()`, and `engine.dispose()`. This is to commit any final changes and close out of everything. Adding if **name = main** is useful and should become a habit for python files. Point this to `main_menu()` so the process may begin. I added some ASCII text art to main menu to spice it up a bit more and help with readability.  I added it with the help of a [text to ascii art converter](https://www.asciiart.eu/text-to-ascii-art).

```python
if __name__ == "__main__":
    main_menu()
```