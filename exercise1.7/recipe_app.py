from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql://cf-python:password@localhost/task_database")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Taken from mySQL
# +--------------+--------------+------+-----+---------+----------------+
# | Field        | Type         | Null | Key | Default | Extra          |
# +--------------+--------------+------+-----+---------+----------------+
# | id           | int          | NO   | PRI | NULL    | auto_increment |
# | name         | varchar(50)  | YES  |     | NULL    |                |
# | ingredients  | varchar(255) | YES  |     | NULL    |                |
# | cooking_time | int          | YES  |     | NULL    |                |
# | difficulty   | varchar(20)  | YES  |     | NULL    |                |
# +--------------+--------------+------+-----+---------+----------------+


class Recipe(Base):
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ": Difficulty = "+ self.difficulty + ">"

    def __str__(self):
        recipe_str = '\n'
        recipe_str += " *" * 4 + " Recipe Name: " + self.name + " " + "* " * 4 + "\n\n"
        recipe_str += "Ingredients list:\n"
        ingredients_list = self.ingredients.split(', ')
        for ingredient in ingredients_list:
            recipe_str += "\t-" + ingredient + "\n"
        recipe_str += "\n>:) Cooking Time: " + str(self.cooking_time) + "\t\n"
        recipe_str += "\n:O Difficulty: " + self.difficulty + '\n'
        return recipe_str

    def calc_difficulty(self):
        # Split the ingredients string into a list
        ingredients_list = self.ingredients.split(", ")

        # Determine the difficulty based on cooking time and number of ingredients
        if self.cooking_time < 10 and len(ingredients_list) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(ingredients_list) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(ingredients_list) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

Base.metadata.create_all(engine)

def create_recipe():
    name = input("Please enter new recipe name: ")
    cooking_time = int(input("Please enter the approximate cooking time in minutes: "))


    # This will run if name is filled in with letters AND if cooking time is a number above 0
    if len(name) > 0  and cooking_time > 0:

        #Create a temporary list to store the ingredients given by the user
        ingredients_temp = []
        ingredient_count = int(input("How many ingredients will you be entering? "))
        print('Enter Ingredients:')
        for _ in range(ingredient_count):
            ingredient = input("-->")
            ingredients_temp.append(ingredient)

        #join the ingredients into a string separated by commas
        ingredients = ', '.join(ingredients_temp)

        #add a new recipe and calculate its difficulty
        new_recipe = Recipe(name=name,ingredients=ingredients,cooking_time=cooking_time)
        new_recipe.calc_difficulty()

        session.add(new_recipe)

        try:
            session.commit()
            print('Recipe Created')
            return None

        except Exception as err:
            session.rollback()
            print('Error: ',err)

    elif cooking_time < 0:
        print('Please try again and enter a valid cooking time')
    else:
        print('Please try again and enter a valid recipe name')

    print('Going back to Main Menu')
    return None
    

def view_all_recipes():
    recipes_list = session.query(Recipe).all()
    if len(recipes_list) < 1:
        print('No Recipes yet.  Go add some!')
        return None

    else:
        for recipe in recipes_list:
            print(recipe)

def search_by_ingredients():
    if session.query(Recipe).count() < 1:
        print('No Recipes yet.  Go add some!')
        return None

    results = session.query(Recipe.ingredients).all()
    all_ingredients = []

    for row in results:
        ingredients_list = row[0].split(",")
        for ingredient in ingredients_list:
            if ingredient.strip() not in all_ingredients:
                all_ingredients.append(ingredient.strip())

    # Display all ingredients with a number
    print("Available Ingredients:")
    for index, ingredient in enumerate(all_ingredients, start = 1):
        print(f"{index}. {ingredient}")

    # Prompt the user to select the ingredient by entering the number
    selected_index = input("Enter each number you wish to search by (separated by spaces): ")
    #split each number, change them to int and put them into a new list
    search_nums = [int(num) for num in selected_index.split()]

    #Change each number to the ingredient by going through the all_ingredients index
    search_ingredients = [all_ingredients[num-1] for num in search_nums]

  
    conditions = []
    #Loop through all recipes
    for recipe in session.query(Recipe).all():
        #Create a list of ingredients that are stripped of white space and stored in ingredient_list
        ingredients_list = [ingredient.strip() for ingredient in recipe.ingredients.split(',')]
        #iterates through all ingredients the user input and checks if they are in the current recipe by going through its ingredient_list
        if all(ingredient in ingredients_list for ingredient in search_ingredients):
            conditions.append(recipe)

    if conditions:
        print("Matching Recipes:")
        for recipe in conditions:
            print(recipe)
    else:
        print("No recipes found with the specified ingredients.")


    #ZZZ I made this in case all recipes that have even on ingredient is supposed to be shown
    # conditions = []
    # for ingredient in search_ingredients:
    #     conditions.append(session.query(Recipe).filter(Recipe.ingredients.like(f"%{ingredient}%")).all())

    # for recipes in conditions:
    #     for recipe in recipes:
    #         print(recipe)
    #     print()



def edit_recipe():
    if session.query(Recipe).count() < 1:
        print('No Recipes yet.  Go add some!')
        return None

    results = session.query(Recipe).all()

    for recipe in results:
        print(recipe.__repr__())

    chosen_id = int(input('Please choose a recipe by typing its recipe ID: '))
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == chosen_id).one()

    if recipe_to_edit:
        print(recipe_to_edit)
        print('Please choose which part of the recipe you would like to update')
        print('1. Name')
        print('2. Ingredients')
        print('3. Cooking Time')
        chosen_edit = int(input("Enter your choice by typing '1', '2', or '3': "))

        if chosen_edit == 1:
            # ZZZ recipe_to_edit.update({Recipe.name: new_name}) /AttributeError: 'Recipe' object has no attribute 'update'
            # Get an error when using update so I do this now
            new_name = input('Please type the new name: ')
            if len(new_name) > 0:
                recipe_to_edit.name = new_name
            else:
                print('Please enter a valid name.')
            
        elif chosen_edit == 2:
             #Create a temporary list to store the ingredients given by the user
            ingredients_temp = []
            ingredient_count = int(input("How many ingredients will you be entering? "))
            print('Enter Ingredients:')
            for _ in range(ingredient_count):
                ingredient = input("-->")
                ingredients_temp.append(ingredient)

            #join the ingredients into a string separated by commas
            new_ingredients = ', '.join(ingredients_temp)

            recipe_to_edit.ingredients = new_ingredients
            recipe_to_edit.calc_difficulty()
            

        elif chosen_edit == 3:
            new_cooking_time = int(input('Please enter a new cooking time: '))
            if new_cooking_time > 0:
                recipe_to_edit.cooking_time = new_cooking_time
                recipe_to_edit.calc_difficulty()
                
            else:
                print('Please enter a number above 0')

        else:
            print("Please enter the number '1', '2', or '3'")

        session.commit()

    else:
        print('Recipe ID not found, please choose from the list')


def delete_recipe():
    if session.query(Recipe).count() < 1:
        print('No Recipes yet.  Go add some!')
        return None

    
    recipes = session.query(Recipe).all()

    for recipe in recipes:
        print(recipe.__repr__())

    chosen = int(input('Please enter the ID of the recipe you would like to remove: '))
    remove_rec = session.query(Recipe).filter(Recipe.id == chosen).one()

    if remove_rec:
        confirm = input(f'Would you like to remove {remove_rec.name}? Please enter yes or no. ').lower()
        if confirm == 'yes':
            session.delete(remove_rec)
            session.commit()
            print('Recipe Removed!')
        else:
            print('Recipe NOT removed')

    else:
        print('No Recipe with that ID was found, please choose from the list!')


def main_menu():
    choice = ''

    while choice != "quit":
        print("""
    ////////////////////////////////////////////////////////////////////////////
    //                                                                        //
    //  /'\_/`\            __              /'\_/`\                            //
    // /\      \     __   /\_\    ___     /\      \     __    ___   __  __    //
    // \ \ \__\ \  /'__`\ \/\ \ /' _ `\   \ \ \__\ \  /'__`\/' _ `\/\ \/\ \   //
    //  \ \ \_/\ \/\ \L\.\_\ \ \/\ \/\ \   \ \ \_/\ \/\  __//\ \/\ \ \ \_\ \  //
    //   \ \_ \ \_\ \__/.\_ \ \_\ \_\ \_\   \ \_\  \_\ \____\ \_\ \_\ \____/  //
    //    \/_/ \/_/\/__/\/_/ \/_/\/_/\/_/    \/_/ \/_/\/____/\/_/\/_/\/___/   //
    //                                                                        //
    ////////////////////////////////////////////////////////////////////////////
        """)
        print("==============================")
        print("What would you like to do? ")
        print("1. Add a new recipe!")
        print("2. View all ingredients")
        print("3. Search through recipes by requested ingredient.")
        print("4. Update a recipe.")
        print("5. Remove a recipe from your recipe book.")
        print("Type 'done' when you are finished.")
        choice = input("Please input a number or 'quit': ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            print("Bye Bye!")
            break
        else:
            print("Please input one of the options listed or 'quit' if you would like to exit.")

        session.commit()

    session.close()
    engine.dispose()

if __name__ == "__main__":
    main_menu()