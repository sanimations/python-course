class Recipe():

    all_ingredients = []

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = self.calc_difficulty()
        
    def calc_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            return 'Easy'
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            return 'Medium'
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            return 'Intermediate'
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
            return 'Hard'

    def get_name(self):
        output = 'This recipe is called: ' + self.name
        return output

    def set_name(self):
        self.name = input('Recipe Name: ')

    def get_cooking_time(self):
        output = 'This recipe takes about ' + self.cooking_time + ' minutes.'
        return output

    def set_cooking_time(self):
        self.cooking_time = int(input('Cooking Time: '))

    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()


    def get_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        ingredients_str = ', '.join(self.ingredients)
        output = f"Name: {self.name}\nIngredients List: {ingredients_str}\nCooking Time: {self.cooking_time} minutes\nDifficulty Level: {self.difficulty}"
        return output

    def recipe_search(data, search_term):
        found = False
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
                found = True
        if not found:
            print('No recipes found containing ' + search_term)

#Main Code

tea = Recipe("Tea", ['Tea Leaves', 'Sugar', 'Water'], 5)
print('Printed Tea:', tea)
coffee = Recipe("Coffee", ['Coffee Powder', 'Sugar', 'Water'], 5)
cake = Recipe("Cake", ['Butter', 'Sugar', 'Eggs', 'Vanilla Extract', 'Flour', 'Baking Powder', 'Milk'], 50)
banana_smoothie = Recipe("Banana Smoothie", ['Bananas', 'Milk', 'Sugar', 'Peanut Butter', 'Ice Cubes'], 5)

recipes_list = [tea, coffee, cake, banana_smoothie]

Recipe.recipe_search(recipes_list, 'Water')
Recipe.recipe_search(recipes_list, 'Sugar')
Recipe.recipe_search(recipes_list, 'Bananas')
