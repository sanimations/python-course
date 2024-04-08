import mysql.connector

conn = mysql.connector.connect(host="localhost", user="cf-python", passwd="password")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Recipes(
    id                  INT PRIMARY KEY AUTO_INCREMENT,
    name                VARCHAR(50),
    ingredients         VARCHAR(255),
    cooking_time        INT,
    difficulty          VARCHAR(20)
)"""
)

def calc_difficulty(ingredients, cooking_time):
    # Split the ingredients string into a list
    ingredients_list = ingredients.split(",")

    # Determine the difficulty based on cooking time and number of ingredients
    if cooking_time < 10 and len(ingredients_list) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients_list) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients_list) < 4:
        return "Intermediate"
    else:
        return "Hard"


def create_recipe(cursor):
    r_name = input("Please enter new recipe name: ")
    r_ingredients = input("Please enter all ingredients separated by commas: ").lower()
    r_cooking_time = int(input("Please enter the approximate cooking time in minutes: "))
    r_difficulty = calc_difficulty(r_ingredients, r_cooking_time)

    new_recipe = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (r_name, r_ingredients, r_cooking_time, r_difficulty)
    cursor.execute(new_recipe, val)
    conn.commit()

    print("Recipe added successfully!")


# Search recipe by Ingredient
def search_recipe(cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = []
    for row in results:
        ingredients_list = row[0].split(",")
        for ingredient in ingredients_list:
            if ingredient.strip() not in all_ingredients:
                all_ingredients.append(ingredient.strip())

    # Display all ingredients with a number
    print("Available Ingredients:")
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(f"{index}. {ingredient}")

    # Prompt the user to select the ingredient by entering the number
    selected_index = int(input("Enter the ingredient's number you wish to search by: ")) -1

    if selected_index < 0 or selected_index >= len(all_ingredients):
        print("Please enter a valid number.")
        return
    else:
        search_ingredient = all_ingredients[selected_index]

    # Construct the SQL query to search for recipes containing the selected ingredient
    query = "SELECT * FROM Recipes WHERE LOWER(ingredients) LIKE %s"

    # Execute the query with the ingredient as a parameter
    cursor.execute(query, ("%" + search_ingredient + "%",))

    # Fetch all the matching recipes
    matching_recipes = cursor.fetchall()

    # Print the matching recipes
    if matching_recipes:
        print("Matching Recipes:")
        for recipe in matching_recipes:
            print("- Recipe ID:", recipe[0])
            print("  Name:", recipe[1])
            print("  Ingredients:", recipe[2])
            print("  Cooking Time:", recipe[3])
            print("  Difficulty:", recipe[4])
            print()
    else:
        print("No recipes found with the ingredient:", search_ingredient)

def update_recipe(cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    for recipe in results:
        print("- Recipe ID:", recipe[0])
        print("  Name:", recipe[1])
        print("  Ingredients:", recipe[2])
        print("  Cooking Time:", recipe[3])
        print("  Difficulty:", recipe[4])
        print()

    # Prompt the user for old and new recipe information
    update_name = input("Please enter the name of the recipe you would like to update: ")
    update_key = input("What section would you like to update?  Please type 'name', 'ingredients', or 'cooking_time': ")
    update_value = input("Please enter the new value: ")


    allowed_updates = ['name', 'ingredients', 'cooking_time']
    if update_key not in allowed_updates:
        print('Invalid section')
        update_recipe(cursor)
        return

    if update_key == 'cooking_time':
        update_value = int(update_value)

        cursor.execute("SELECT ingredients FROM Recipes WHERE name = %s", (update_name,))
        current_ingredients = cursor.fetchone()[0]
        update_difficulty = calc_difficulty(current_ingredients, update_value)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE name = %s", (update_difficulty, update_name))

    if update_key == 'ingredients':
        cursor.execute("SELECT cooking_time FROM Recipes WHERE name = %s", (update_name,))
        current_cooking_time = cursor.fetchone()[0]
        update_difficulty = calc_difficulty(update_value, current_cooking_time)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE name = %s", (update_difficulty, update_name))


    update_query = f"UPDATE Recipes SET {update_key} = %s WHERE name = %s"
    cursor.execute(update_query, (update_value, update_name))
    print("Recipe updated successfully.")


def delete_recipe(cursor):
    # Prompt the user for which recipe they would like removed
    delete_rec = input("Please enter recipe name you wish to remove: ")
    cursor.execute("DELETE FROM Recipes WHERE name = %s", (delete_rec,))
    print("Recipe Removed")


def main_menu(conn, cursor):
    choice = ''

    while choice != "done":
        print("Main Menu")
        print("==============================")
        print("What would you like to do? ")
        print("1. Add a new recipe!")
        print("2. Search through recipes by requested ingredient.")
        print("3. Update a recipe.")
        print("4. Remove a recipe from your recipe book.")
        print("Type 'done' when you are finished.")
        choice = input("Please input a number or 'done': ")

        if choice == "1":
            create_recipe(cursor)
        elif choice == "2":
            search_recipe(cursor)
        elif choice == "3":
            update_recipe(cursor)
        elif choice == "4":
            delete_recipe(cursor)
        elif choice == "done":
            break
        else:
            print("Please input one of the options listed or 'done' if you would like to exit.")

        conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main_menu(conn, cursor)