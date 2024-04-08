import pickle

def display_recipe(recipe: dict):
    print("Recipe:", recipe['name'])
    print("Cooking Time (min):", recipe['cooking_time'])
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print("Difficulty:", recipe['difficulty'])

def search_ingredient(data: dict):
    print("Ingredients Available Across All Recipes")
    for index, ingredient in enumerate(data['all_ingredients'], start=1):
        print(f"{index}. {ingredient}")

    try:
        chosen_num = int(input("Pick a number from the list: "))
        ingredient_searched = data['all_ingredients'][chosen_num - 1]
    except ValueError:
        print('Invalid input: Please enter a number.')
    except IndexError:
        print('Invalid number: Please select a number within the range.')
    except Exception as e:
        print(f'An error occured: {e}')
    else:
        found = False
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found = True
        if not found:
            print('No recipe with that ingredient')


fileName = input("Enter the name of the file containing your recipe data: ")

try:
    with open(fileName, 'rb') as my_file:
        data = pickle.load(my_file)
except FileNotFoundError:
    print("File not found.")
else:
    search_ingredient(data)