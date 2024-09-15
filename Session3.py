# Python Tutorial: Lists, Loops, and Tuples
# This tutorial covers basic operations on lists, loops, and tuples.

# -----------------------------
# 1. Lists
# Lists are a collection of items in a particular order, defined with square brackets [].
# Items in a list can be of any type (strings, numbers, etc.).
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("Original list of bicycles:", bicycles)

# Accessing elements in a list by index
# Python uses zero-based indexing, meaning the first element is at index 0.
print("First bicycle:", bicycles[0].upper())  # Using upper() to capitalize

# Finding the length of a list using len() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Number of cars in the list:", len(cars))

# -----------------------------
# 2. Modifying a List
# You can modify elements in a list by accessing them via their index.
# Changing an element at a specific index.
bicycles[0] = 'giant'
print("Updated list of bicycles:", bicycles)

# -----------------------------
# 3. Adding Elements to a List
# You can append elements to the end of the list using append().
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print("List after appending:", motorcycles)

# You can insert an element at a specific position using insert().
motorcycles.insert(0, 'harley')
print("List after inserting at index 0:", motorcycles)

# -----------------------------
# 4. Removing Elements from a List
# Removing by index using del.
del motorcycles[0]
print("List after using del:", motorcycles)

# Using pop() to remove and return the last element (or at a specific index).
popped_motorcycle = motorcycles.pop()
print("Popped motorcycle:", popped_motorcycle)
print("List after popping:", motorcycles)

# Removing by value using remove().
motorcycles.remove('yamaha')
print("List after removing 'yamaha':", motorcycles)

# -----------------------------
# 5. Sorting a List
# Sorting a list permanently using sort().
cars.sort()
print("Permanently sorted cars:", cars)

# Sorting temporarily using sorted().
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original list of cars:", cars)
print("Temporarily sorted cars:", sorted(cars))
print("Original list after temporary sort:", cars)

# -----------------------------
# 6. Reversing the Order of a List
# Reversing the order of elements using reverse().
cars.reverse()
print("Reversed list of cars:", cars)

# -----------------------------
# 7. Avoiding Index Errors
# Index errors occur when trying to access an element that doesn’t exist in the list.
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])  # This would raise an IndexError because the list has only 3 elements.

# -----------------------------
# 8. For Loops
# A for loop iterates over the elements of a list.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Post-loop code
print("Thank you everyone. That was a great magic show!")

# -----------------------------
# 9. Working with Numerical Lists
# Using range() to generate a sequence of numbers.
for value in range(1, 5):
    print("Generated value:", value)

# Creating a list from a range of numbers.
numbers = list(range(1, 6))
print("List of numbers:", numbers)

# -----------------------------
# 10. List Comprehension
# A concise way to generate a list.
squares = [value ** 2 for value in range(1, 6)]
print("List of squares:", squares)

# -----------------------------
# 11. Tuples
# A tuple is an immutable list, defined using parentheses ().
dimensions = (200, 50)
print("Tuple dimensions:", dimensions)

# Accessing elements in a tuple works just like lists.
print("First dimension:", dimensions[0])

# Tuples are immutable, so attempting to modify them will cause an error:
# dimensions[0] = 250  # This will raise a TypeError.

# -----------------------------
# 12. Looping Through a Tuple
# You can loop through the elements of a tuple just like a list.
for dimension in dimensions:
    print("Dimension:", dimension)

# -----------------------------
# 13. Modifying a Tuple
# Tuples cannot be modified, but you can assign a new tuple to the same variable.
dimensions = (400, 100)
print("New tuple dimensions:", dimensions)