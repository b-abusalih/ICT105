# Python Tutorial: Functions

# ------------------------------------------
# 1. Defining and Calling Functions
# Functions are reusable blocks of code. Use the def keyword to define a function.

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

# Call the function
greet_user()  # Output: Hello!

# ------------------------------------------
# 2. Passing Information to a Function
# Functions can accept parameters to make them more flexible.

def greet_user(username):
    """Display a personalized greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')  # Output: Hello, Jesse!

# ------------------------------------------
# 3. Positional Arguments
# The order of arguments matters in positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# ------------------------------------------
# 4. Keyword Arguments
# Keyword arguments are name-value pairs that eliminate confusion about parameter order.

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')

# ------------------------------------------
# 5. Default Values
# Use default values for parameters that typically take the same value.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet with a default animal type."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')           # Uses the default value 'dog'
describe_pet('harry', 'hamster') # Overwrites the default value

# ------------------------------------------
# 6. Return Values
# Functions can process data and return a result using the return statement.

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Output: Jimi Hendrix

# ------------------------------------------
# 7. Optional Arguments
# You can make arguments optional by giving them default values, like an empty string.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, optionally including a middle name."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_formatted_name('john', 'hooker', 'lee'))
print(get_formatted_name('jimi', 'hendrix'))

# ------------------------------------------
# 8. Returning a Dictionary
# Functions can return complex data structures like dictionaries.

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)  # Output: {'first': 'jimi', 'last': 'hendrix', 'age': 27}

# ------------------------------------------
# 9. Using Functions with while Loops
# You can use functions in a loop to repeatedly prompt for user input.

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# ------------------------------------------
# 10. Passing a List
# Functions can accept lists and work with their contents.

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        print(f"Hello, {name.title()}!")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# ------------------------------------------
# 11. Modifying a List in a Function
# Passing a list to a function allows the function to modify the list directly.

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design until none are left."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# ------------------------------------------
# 12. Passing an Arbitrary Number of Arguments
# The * symbol allows a function to accept any number of arguments.

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# ------------------------------------------
# 13. Mixing Positional and Arbitrary Arguments
# You can mix a regular positional parameter with an arbitrary number of additional arguments.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# ------------------------------------------
# 14. Using Arbitrary Keyword Arguments
# The ** symbol allows a function to accept any number of key-value pairs.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# ------------------------------------------
# 15. Storing Functions in Modules
# Save a function in a separate file (module) and import it into the main program.
# In a separate file called pizza.py:

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Then in the main program, import and use this function.
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# ------------------------------------------
# Lab Exercises
# ------------------------------------------
# 1. T-Shirt Function
def make_shirt(size, message):
    """Summarize the shirt that is going to be made."""
    print(f"\nMaking a {size} shirt with the message: '{message}'.")

# Positional arguments
make_shirt('Large', 'I love Python!')

# Keyword arguments
make_shirt(size='Medium', message='Code is life!')

# 2. User Profile
user_profile = build_profile('bilal', 'abu-salih', location='perth', field='information systems')
print(user_profile)

# 3. Describe City Function
def describe_city(city, country='Australia'):
    """Describe a city and its country."""
    print(f"{city.title()} is in {country}.")

describe_city('Sydney')
describe_city('Reykjavik', 'Iceland')
describe_city('Tokyo', 'Japan')
