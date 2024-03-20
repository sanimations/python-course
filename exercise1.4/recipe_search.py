import pickle

def display_recipe(recipe : dict):
    print("Recipe:", recipe['name'])
    print("Cooking Time (min):", recipe['cooking_time'])
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print("Difficulty:", recipe['difficulty'])

def search_ingredient(data : dict):
    print("Ingredients Available Across All Recipes")
    for index, ingredient in enumerate(data['ingredients_list'], start=1):
    print(f"{index}. {ingredient}")

    try:
        chosen_num = int(input("Pick a number from the list: "))
        ingredient_searched = data['ingredients_list'][chosen_num]
    except:
        print('Invalid number')
    else:
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                print(recipe['name'] + '\n')
            else:
                print('No recipe with that ingredient')


