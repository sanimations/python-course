recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Recipe Name: ")
    cooking_time = int(input("Cooking time: "))
    ingredients = input("Enter Ingredients (separated by commas): ").split(',')
    recipe = {
        'name' : name,
        'cooking_time' : cooking_time,
        'ingredients' : ingredients
    }
    return recipe


n = int(input("How many recipes would you like to enter? "))

for x in range(n):
    recipe = take_recipe()

    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time']<10 and len(recipe['ingredients'])<4:
        difficulty = "Easy"
    elif recipe['cooking_time']<10 and len(recipe['ingredients'])>=4:
        difficulty = "Medium"
    elif recipe['cooking_time']>=10 and len(recipe['ingredients'])<4:
        difficulty = "Intermediate"
    elif recipe['cooking_time']>=10 and len(recipe['ingredients'])>=4:
        difficulty = "Hard"

    recipe['difficulty'] = difficulty

for recipe in recipes_list:
    print("Recipe:", recipe['name'])
    print("Cooking Time (min):", recipe['cooking_time'])
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print("Difficulty:", recipe['difficulty'])

print("Ingredients Available Across All Recipes")
for ingredient in ingredients_list:
    print(ingredient)