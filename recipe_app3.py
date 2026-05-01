"""
A simple command-line recipe application that allows users to input their available ingredients and see which recipes they can make based on those ingredients.

Features:
1. Add ingredients to the user's list.
2. View the user's current list of ingredients.
3. View all available recipes.
4. Display recipes that the user can make with their current ingredients.
5  View Recipes by dietary preferences
6. Exit the application.
"""

# Recipe class in order to sort by various dietary restirctions or personal prefernces for the user.
class Recipe: 
    def __init__(self, name, ingredients):
        self.name = name

        self.ingredients = ingredients
    
        self.contains_dairy = any(
            item in ingredients for item in ["milk", "cheese", "butter", "yogurt"]
        )
        self.contains_gluten = any(
            item in ingredients for item in ["bread", "flour", "noodles", "dough", "tortilla"]
        )
        self.vegetarian = "meat" not in ingredients

# this acts as our "database" of recipes, with the recipe name represented as the key and a list of required ingredients as the value
# converted from dictionary in order to sort recipes into different classes to differentiate by dietary restrictions. 
recipes = [
    Recipe("omelette", ["eggs", "milk", "cheese"]),
    Recipe("PB&J", ["bread", "peanut butter", "jelly"]),
    Recipe("toast", ["bread", "butter"]),
    Recipe("mac and cheese", ["noodles", "cheese", "milk"]),
    Recipe("salad", ["lettuce", "tomatoes", "cucumbers", "dressing"]),
    Recipe("smoothie", ["fruit", "yogurt", "milk"]),
    Recipe("pasta", ["noodles", "sauce", "cheese"]),
    Recipe("grilled cheese", ["bread", "cheese", "butter"]),
    Recipe("tacos", ["tortillas", "meat", "cheese", "lettuce", "salsa"]),
    Recipe("pizza", ["dough", "sauce", "cheese"]),
    Recipe("soup", ["broth", "vegetables", "meat"]),
    Recipe("stir fry", ["vegetables", "meat", "sauce"]),
    Recipe("curry", ["meat", "vegetables", "curry sauce"]),
    Recipe("sandwich", ["bread", "meat", "cheese", "lettuce", "tomatoes"]),
    Recipe("burrito", ["tortilla", "meat", "rice", "beans", "cheese", "salsa"]),
    Recipe("pancakes", ["flour", "milk", "eggs", "syrup"]),
    Recipe("waffles", ["flour", "milk", "eggs", "syrup"]),
    Recipe("quiche", ["eggs", "milk", "cheese", "vegetables"]),
    Recipe("frittata", ["eggs", "milk", "cheese", "vegetables"]),
    Recipe("casserole", ["meat", "vegetables", "cheese", "sauce"]),
    Recipe("lasagna", ["noodles", "meat", "sauce", "cheese"]),
    Recipe("chili", ["meat", "beans", "tomatoes", "spices"]),
]

# will hold all user submitted ingredients, by default this is empty.
user_ingredients: list[str] = []

# Main loop to interact with the user, and at the current development state the rest of the applications functionality. Looping indefinitely here is fine due to the 5th option breaking out of the loop and exiting the program entirely.
while True:
    # read_recipe_csv()  # this function is currently a placeholder for future development, it will be used to read in recipes from a csv file and populate our recipes dictionary, but for now it does nothing and is just here to show where that functionality will be added in the future.
    # add_new_recipe() # save new thing to recipe.csv

    # make assumptions about how refactor will go
    # assume csv is returned as standard
    # remove and possibly updating existing

    print("\n1. Add an ingredient")
    print("2. View my ingredients")
    print("3. View all available recipes")
    print("4. Display recipes I can make")
    print("5. View recipes by dietary preference")
    print("6. Exit")

    user_input: str = input("\n Choose an option: (1-6)")

    if user_input == "1":
        print("\nEnter ingredients one by one (type 'done' when finished):")

        # loop below takes in the user input and converts it to lowercase while also removing any trailing or leading white space, text passed to input is purely cosmetic
        # We use an infinite loop here so that the user may input multiple ingredients without returning to the main menu. Checking for the string "done" allows the user to control when they are finished. Otherwise the new string is added to the users list of ingredients, unless it already exists, which the last portion of the conditional will check for
        # Functions learned outsite of class: lower(), strip(). Used to take user input and set it to lowercase and remove any leading or trailing whitespace to ensure consistency in the ingredient list and avoid bugs as we check what is submitted.
        # keywords learned outside of class: break, not, and, in. User for control flow and deciding what to do with user_input
        #
        while True:
            item = input(">>> ").lower().strip()
            if item == "done":
                break
            elif item and item not in user_ingredients:
                user_ingredients.append(item)
            elif item in user_ingredients:
                print(f"{item} is already in your ingredient list.")
            else:
                print("Please enter a valid ingredient or type 'done' to finish.")

    elif user_input == "2":
        print("\nMy Ingredients:")
        if not user_ingredients:
            print("- (none)")
        for ingredient in user_ingredients:
            print(f"- {ingredient}")

    # conditional below will iterate through our recipe dictionary and print out each key, which will be the name of the recipe
    # Functions learned outside of class: keys(). Returns a set containing all keys in a dictionary, which in our case are recipe names
    # Updated to work with new classes
    elif user_input == "3":
        print("\nAvailable Recipes:")
        for recipe in recipes:
            print(f"- {recipe.name}")

    # conditional below will iterate through our recipe dictionary and check if all the ingredients required for a recipe are present in the user's ingredient list. If they are, it will print out the name of the recipe as a possible option for the user to make with their current ingredients.
    # Functions learned outside of class: items(). Used on a dictionary to return a tuple of key-value pairs, which we use to check each recipe and it's ingredients against the user's list of ingredients.'
    # Concepts learned outside of class: Nested loops. Unpacking (mentioned briefly in class when taught about tuples, can be used here due to items() returning a tuple of key-value pairs)
    elif user_input == "4":
        print("\nPossible Recipes with your ingredients:")

        for recipe in recipes:
            has_all_ingredients = True  # this will be our flag to determine if a users ingredients already exists

            # if the ingredient does not exist in the user_ingredients list, we will set our has_all_ingredients flag to false and leave the loops
            for ingredient in recipe.ingredients:
                if ingredient not in user_ingredients:
                    has_all_ingredients = False
                    break

            # if flag is not changed to false, we print the recipe
            if has_all_ingredients:
                print(f"- {recipe.name}")

    elif user_input == "5":
        print("\nDietary Options:")
        print("1. Contains dairy")
        print("2. Contains gluten")
        print("3. Vegetarian")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
#this is where users run thorugh dietary options that they can view recipes of 
        if choice == "1":
            print("\nRecipes with dairy:")
            for recipe in recipes:
                if recipe.contains_dairy:
                    print(f"- {recipe.name}")

        elif choice == "2":
            print("\nRecipes with gluten:")
            for recipe in recipes:
                if recipe.contains_gluten:
                    print(f"- {recipe.name}")

        elif choice == "3":
            print("\nVegetarian recipes:")
            for recipe in recipes:
                if recipe.vegetarian:
                    print(f"- {recipe.name}")

        elif choice == "4":
            continue

    elif user_input == "6":
        print("Goodbye!")
        break


def read_recipe_csv():
    pass