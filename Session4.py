# Python Tutorial: Conditional Statements and Loops

# ------------------------------------------
# 1. Conditional Tests
# Every `if` statement in Python checks a condition that evaluates to either True or False.

# Example:
number = 5
if number > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")

# ------------------------------------------
# 2. if-elif-else Chains
# These are useful when you need to check multiple conditions.

age = 70

if age < 4:
    price = 0  # Free admission for toddlers
elif age < 18:
    price = 25  # Reduced price for kids and teenagers
elif age < 65:
    price = 40  # Standard adult price
else:
    price = 20  # Discount for elders

print(f"Your admission cost is ${price}.")


# Another example to evaluate the grade of a student

marks = 70

if marks >= 90 :
    grade = 'High Distinction' 
elif marks >= 80 :
    grade = 'Distinction'
elif marks >= 70 :
    grade = 'Credit' 
elif marks >= 60 :
    grade = 'Pass'
else:
    grade = 'Fail!'

print (f"Student's grade with the total marks of {marks} is\
 {grade}")


# ------------------------------------------
# 3. Multiple Conditions
# You can use multiple `if` statements to check several conditions independently.
# Unlike if-elif-else, each condition is checked separately.

toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in toppings:
    print("Adding mushrooms.")

if 'extra cheese' in toppings:
    print("Adding extra cheese.")

# ------------------------------------------
# 4. Using If Statements in Loops
# Loops can be combined with conditionals to perform actions repetitively with decision-making.

toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers.")
    else:
        print(f"Adding {topping}.")

# ------------------------------------------
# 5. Checking for Empty Lists Before Looping
# It’s a good idea to check if a list is empty before iterating over it to avoid errors.


toppings = []
if toppings:
    for topping in toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")

# ------------------------------------------
# 6. Validating Inputs Against Expected Values
# Use conditionals to validate user input 
# against a predefined list of valid options.

available_toppings = ['mushrooms', 'olives', 'green peppers', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we don't have {topping}.")

# ------------------------------------------
# Summary:
# - `if` statements allow for decision-making by checking conditions.
# - `if-elif-else` chains help in choosing one action from multiple possibilities.
# - Loops are used for repeating actions, and when combined with conditionals, they can perform complex tasks.
# - Always validate inputs and check lists before iterating over them to avoid errors.
