"""
A simple command-line recipe application that allows users to input their available ingredients and see which recipes they can make based on those ingredients.

Features:
1. Add ingredients to the user's list.
2. View the user's current list of ingredients.
3. View all available recipes.
4. Display recipes that the user can make with their current ingredients.
5. View recipes by dietary preference
6. Exit the application.

ingredient_list is loaded with cheese, eggs, milk, and apples to demonstrate reading of an already existing file. File will be updated by the app and can be deleted to demonstrate creating a new file when none exists

TO SAVE YOU HAVE TO EXIT THE APP (option 6)!
"""

# will hold all user submitted ingredients, by default this is empty.
user_ingredients: list[str] = []

# this will hold all our recipes and incredients, allowing for saving and changing after the app is closed
recipes: list["Recipe"] = []


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


def get_recipes_from_file(filename: str) -> None: 
    """
    Loads recipe file and saves into recipe variable
    """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    # for line in lines[1:]:  # skip header
    for line in lines:
        parts = line.strip().split(",")
        name = parts[0]
        ingredients = [i for i in parts[1:] if i != ""]



def save_ingredients_to_file(filename: str) -> None:
    """
    Saves the user's list of ingredients to a separate file using after the app is closed
    """
    file = open(filename, "w")
    for ingredient in user_ingredients:
        file.write(f"{ingredient} \n")
        print(f"{ingredient} saved to file.")
    file.close()


def load_ingredient_list(filename: str) -> None:
    """
    Loads the user's list of ingredients from a separate file when the app is opened, allowing them to continue where they left off     Demonstrating the use of a try to show an error if a file does not exist
    """
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            ingredient = line.strip()
            if ingredient and ingredient not in user_ingredients:
                user_ingredients.append(ingredient)
                print(f"{ingredient} loaded from file.")
    except FileNotFoundError:
        print("No saved ingredient list found. Starting with an empty list.")


def display_menu() -> None:
    """
    Displays the main menu and prompts the user for a choice.
    """
    print("1. Add an ingredient")
    print("2. View my ingredients")
    print("3. View all available recipes")
    print("4. Display recipes I can make")
    print("5. View recipes by dietary preference")
    print("6. Exit")


def get_user_choice() -> str:
    """
    Prompts the user for a menu choice then returns that choice (if valid) as a string value.

    try is used to test if the input is a valid number between 1 and 5, if it is not we show a Value error and print out the issue, and return "error" which our app will check for to decide if it should run the function again
    """
    try:
        choice = int(input("\nChoose an option: (1-6) "))
        if 1 <= choice <= 6:
            return str(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            return "error"
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return "error"


def add_ingredient(filename: str) -> None:
    """loop below takes in the user input and converts it to lowercase while also removing any trailing or leading white space, text passed to input is purely cosmetic

    We use an infinite loop here so that the user may input multiple ingredients without returning to the main menu. Checking for the string "done" allows the user to control when they are finished. Otherwise the new string is added to the users list of ingredients, unless it already exists, which the last portion of the conditional will check for

    Functions learned outsite of class: lower(), strip(). Used to take user input and set it to lowercase and remove any leading or trailing whitespace to ensure consistency in the ingredient list and avoid bugs as we check what is submitted.
    keywords learned outside of class: break, not, and, in. User for control flow and deciding what to do with user_input

    Concept learned outside of class: calling a function from another function
    """
    print("\nEnter ingredients one by one (type 'done' when finished):")

    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            ingredient = line.strip()
            if ingredient and ingredient not in user_ingredients:
                user_ingredients.append(ingredient)
    except FileNotFoundError:
        print("No saved ingredient list found. Starting with an empty list.")

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


def show_user_ingredients() -> None:
    print("\nMy Ingredients:")
    for ingredient in user_ingredients:
        print(f"- {ingredient}")


def show_available_recipes() -> None:
    """
    prints all the recipes available in our recipe dictionary, which are the keys of the dictionary
    """
    print("\nAvailable Recipes:")
    for recipe in recipes:
        print(f"- {recipe.name}")


def show_possible_recipes() -> None:
    """
    Shows all recipes that the user can create given the list of ingredients they have added
    """
    print("\nPossible Recipes with your ingredients:")
    for recipe in recipes:
        has_all_ingredients = True

        for ingredient in recipe.ingredients:
            if ingredient not in user_ingredients:
                has_all_ingredients = False
                break

        if has_all_ingredients:
            print(f"- {recipe.name}")


def save_users_new_ingredients(filename: str) -> None:
    """
    Saves the user's new list of ingredients to a separate file using after the app is closed, allowing them to continue where they left off when they open the app again
    """
    file = open(filename, "w")
    for ingredient in user_ingredients:
        file.write(f"{ingredient} \n")
        print(f"{ingredient} saved to file.")
    file.close()


def load_recipes_and_ingredients(recipes_filename: str, ingredients_filename: str) -> None:
    """
    Loads the recipes and ingredients from their respective files when the app is opened, allowing them to continue where they left off

    We can use 2 functions we already wrote at the same time by calling this, which lets us use this at the beginning of the app to make sure we have all the data needed
    """
    get_recipes_from_file(recipes_filename)
    load_ingredient_list(ingredients_filename)


def main() -> None:
    """
    Main loop to interact with the user
    
    Calls functions to load our data from files into variables -> displays the menu -> gets user input -> calls a different function depending on the users input -> saves the users new ingredients into a file when they choose the option to exit before exiting

    """
    display_menu()

    user_input: str = get_user_choice()

    if user_input == "error":
        user_input = get_user_choice()

    if user_input == "1":
        add_ingredient("ingredient_list.txt")

    elif user_input == "2":
        show_user_ingredients()

    elif user_input == "3":
        show_available_recipes()

    elif user_input == "4":
        show_possible_recipes()

    elif user_input == "5":
        print("\nDietary Options:")
        print("1. Contains dairy")
        print("2. Contains gluten")
        print("3. Vegetarian")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

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
            return

    elif user_input == "6":
        print("Goodbye!")
        save_users_new_ingredients("ingredient_list.txt"
        )  # this will save the users new ingredients to a text file so that they can be loaded again when the app is opened again
        exit()  # newly learned python function that is replacing our "break" from project 1 to exit the program if this option is chosen


if __name__ == "__main__":
    while True:
        main()