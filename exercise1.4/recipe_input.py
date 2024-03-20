import pickle

#Creating Global Variables
recipes_list = []
all_ingredients = []

#user notes how many recipes they would like to enter
n = int(input("How many recipes would you like to enter? "))

#iterates through n times for how many recipes the user wants
for x in range(n):
    recipe = take_recipe()

    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            ingredients_list.append(ingredient)
    
    recipes_list.append(recipe)

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

#User inputs filename with .bin
fileName = input("What file are you looking for: ")

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
except:
    data = {
        'recipes_list' : recipes_list,
        'all_ingredients' : all_ingredients
    }
    print('An unknown error occured!')
else:
    print('Data Successfully Loaded')
finally:
    for i in data:
        print('Recipes list: ', data[recipes_list])
        print('All Ingredients ', data[all_ingredients])



my_file = open(fileName, 'wb')
pickle.dump(data, my_file)
my_file.close()