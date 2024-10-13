# Python Tutorial: User Inputs and While Loops

# ------------------------------------------
# 1. Accepting User Input
# The input() function allows the program to take user input and store it as a string.

# Example:
message = input("Tell me something and I will repeat it back to you: ")
print(message)

# ------------------------------------------
# 2. Writing Clear Prompts
# It’s important to write clear prompts to guide the user in entering the desired input.

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# ------------------------------------------
# 3. Using int() for Numerical Input
# The input() function always returns a string, so you need to convert it to an integer for numerical operations.

age = input("How old are you? ")
age = int(age)  # Convert string to integer

if age >= 18:
    print("You are old enough to vote!")
else:
    print("You will be able to vote when you are older.")

# Example program that checks if a user is tall enough to ride a roller coaster:
height = input("How tall are you in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# ------------------------------------------
# 4. The Modulo Operator (%)
# The modulo operator returns the remainder of a division and is commonly used to check if numbers are even or odd.

number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# ------------------------------------------
# 5. Using While Loops
# The while loop runs as long as a condition is True.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1  # Increment to avoid an infinite loop

# ------------------------------------------
# 6. Quitting with User Input
# This loop continues until the user enters 'quit'.

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# ------------------------------------------
# 7. Using a Flag
# A flag variable is used to control the loop’s execution.

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# ------------------------------------------
# 8. Using break to Exit a Loop
# The break statement exits the loop immediately, even if the condition is still True.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# ------------------------------------------
# 9. Using continue to Skip an Iteration
# The continue statement skips the current iteration and goes back to the start of the loop.

current_number = 1
while current_number < 10:
    print(current_number)  # Only odd numbers are printed
    current_number += 2

for number in range(1,10,2):
    print(number)

# ------------------------------------------
# 10. Avoiding Infinite Loops
# Be careful to ensure that your loop has a condition to end, or it will run forever.

x = 10
while x >= 5:
    print(x)
    x -= 1  # Uncommenting this line will create an infinite loop

# ------------------------------------------
# 11. Using while Loops with Lists and Dictionaries
# Moving items from one list to another.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until no unconfirmed users remain
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # Remove the last user from unconfirmed_users
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# ------------------------------------------
# 12. Removing All Instances of a Value from a List
# Using a while loop to remove all instances of a specific value from a list.

    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print("Initial list of pets:", pets)

    while 'cat' in pets:
        pets.remove('cat')

    print("List after removing all 'cat':", pets)

# ------------------------------------------
# 13. Filling a Dictionary with User Input
# Prompt users for their names and favorite mountains, storing the responses in a dictionary.

responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Ask if another user wants to respond
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

# ------------------------------------------
# Lab Exercises
# ------------------------------------------
# 1. Pizza Toppings: Prompt the user to enter pizza toppings until they enter 'quit'.
prompt = "\nEnter a topping to add to your pizza (enter 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza!")

# 2. Movie Tickets: Determine the cost of a ticket based on the user's age.
age = int(input("\nWhat is your age? "))
if age < 3:
    price = 0
elif age <= 12:
    price = 10
else:
    price = 15

print(f"Your ticket price is ${price}.")

# 3. Dream Vacation: Ask users about their dream vacation and display the responses.
vacations = {}

polling_active = True
while polling_active:
    name = input("\nWhat's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    
    vacations[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Dream Vacation Poll Results ---")
for name, place in vacations.items():
    print(f"{name.title()} would like to visit {place.title()}.")
