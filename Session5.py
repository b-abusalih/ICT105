# Python Tutorial: Working with Dictionaries

# ------------------------------------------
# 1. Introduction to Dictionaries
# A Python dictionary is a collection of key-value pairs.
# Keys are unique and are used to access their corresponding values.

# Example:
alien_0 = {'color': 'green', 'points': 5}  # A dictionary with two key-value pairs
print(alien_0['color'])  # Accessing the value associated with the key 'color'
print(alien_0['points'])  # Accessing the value associated with the key 'points'

# ------------------------------------------
# 2. Adding New Key-Value Pairs
# You can add new key-value pairs to a dictionary by specifying the new key and its value.

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)  # The dictionary now has four key-value pairs

# ------------------------------------------
# 3. Starting with an Empty Dictionary
# You can create an empty dictionary and add key-value pairs to it dynamically.

alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = 10
print(alien_1)  # A dictionary with two key-value pairs added later

# ------------------------------------------
# 4. Modifying Values in a Dictionary
# You can modify the value associated with a key in a dictionary by reassigning it.

alien_1['color'] = 'red'  # Changing the color from 'yellow' to 'red'
print(f"The alien is now {alien_1['color']}.")

# You can also use conditionals to modify values dynamically.
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")  # The x_position value is updated

# ------------------------------------------
# 5. Removing Key-Value Pairs
# Use `del` to completely remove a key-value pair from a dictionary.

alien_2 = {'color': 'green', 'points': 5}
print(alien_2)
del alien_2['points']  # Removing the key 'points' and its associated value
print(alien_2)  # Now only the 'color' key remains

# ------------------------------------------
# 6. Using the `get()` Method
# The `get()` method can be used to safely access a key’s value without raising an error if the key doesn’t exist.

alien_3 = {'color': 'green', 'speed': 'slow'}
# This will return 'No point value assigned.' if the key 'points' is not found.
point_value = alien_3.get('points', 'No point value assigned.')
print(point_value)

# ------------------------------------------
# 7. Looping Through a Dictionary
# You can loop through all key-value pairs in a dictionary using a for loop.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

for name, language in favorite_languages.items():  # items() returns key-value pairs
    print(f"{name.title()}'s favorite language is {language.title()}.")

# ------------------------------------------
# 8. Looping Through All Keys
# You can loop through just the keys in a dictionary using the `keys()` method.

for name in favorite_languages.keys():  # Looping through keys
    print(f"Hello, {name.title()}!")

# Looping through keys in a sorted order
for name in sorted(favorite_languages.keys()):  # sorted() returns keys in order
    print(f"{name.title()}, thank you for taking the poll.")

# ------------------------------------------
# 9. Looping Through All Values
# You can loop through all values in a dictionary using the `values()` method.

print("The following languages have been mentioned:")
for language in favorite_languages.values():  # values() returns values
    print(language.title())

# ------------------------------------------
# 10. Finding Unique Values with `set()`
# To get unique values from the dictionary, use the `set()` function to remove duplicates.

print("Unique languages mentioned:")
for language in set(favorite_languages.values()):  # set() removes duplicates
    print(language.title())

# ------------------------------------------
# 11. Nesting Dictionaries
# You can nest dictionaries inside lists, lists inside dictionaries, or dictionaries inside other dictionaries.

# Example 1: List of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]  # A list of dictionaries
for alien in aliens:
    print(alien)

# Example 2: List of dictionaries dynamically generated
aliens = []
for alien_number in range(30):  # Generate a list of 30 aliens
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Modify some aliens
for alien in aliens[:3]:  # Modify the first 3 aliens
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

# Example 3: List in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# ------------------------------------------
# 12. Dictionary in a Dictionary
# You can nest a dictionary inside another dictionary.

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")



