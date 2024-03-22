import pickle

#Creating Global Variables
recipes_list = []
all_ingredients = []

# Calculates difficulty
def calc_difficulty(recipe):
    if recipe['cooking_time']<10 and len(recipe['ingredients'])<4:
        return "Easy"
    elif recipe['cooking_time']<10 and len(recipe['ingredients'])>=4:
        return "Medium"
    elif recipe['cooking_time']>=10 and len(recipe['ingredients'])<4:
        return "Intermediate"
    elif recipe['cooking_time']>=10 and len(recipe['ingredients'])>=4:
        return "Hard"

# Takes recipe inputs and stores it in a dictionary, adding difficulty last
def take_recipe():
    name = input("Recipe Name: ")
    cooking_time = int(input("Cooking time: "))
    ingredients = input("Enter Ingredients (separated by commas): ").split(',')
    recipe = {
        'name' : name,
        'cooking_time' : cooking_time,
        'ingredients' : ingredients
    }
    recipe['difficulty'] = calc_difficulty(recipe)
    return recipe


#user notes how many recipes they would like to enter
n = int(input("How many recipes would you like to enter? "))

#iterates through n times for how many recipes the user wants
for x in range(n):
    recipe = take_recipe()

    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    
    recipes_list.append(recipe)


#User inputs filename with .bin
fileName = input("Enter a filename with .bin to save recipes (if none exist, a file will be created): ")

#Trying the try, except it's difficult.  Makes sense or else I would finally be done.
#Opens file with the name given, if file not found, it will create a data dictionary
try:
    with open(fileName, 'rb') as my_file:
        data = pickle.load(my_file)
except FileNotFoundError:
    data = {
        'recipes_list' : recipes_list,
        'all_ingredients' : all_ingredients
    }
    print('File Not Found! Creating new file now...')
except Exception as e:
    data = {
        'recipes_list' : recipes_list,
        'all_ingredients' : all_ingredients
    }
    print(f'An error occured: {e}')
else:
    print('Data Successfully Loaded')
finally:
    print('Recipes list: ', data["recipes_list"])
    print('All Ingredients ', data["all_ingredients"])


try:
    with open(fileName, 'wb') as my_file:
        pickle.dump(data, my_file)
        print('Data successfully saved.')
except Exception as e:
    print(f'An error occurred while saving data: {e}')