
# Python Language Basics

# 1. Understanding Syntax:
# Python uses indentation to define blocks of code. It makes the syntax clean and readable.
x = 5

if x < 10:
    print("x is less than 10")
else:
    print("x is 10 or more")

# Variables

# 2. Declaring Variables:
# In Python, variables are declared and assigned using the equals sign. No type declaration is needed.
message = "Hello, Python!"
print(message)

# 3. Local vs Global Variables
# Local variables are accessible only within the function where they are defined:
def my_function():
    x = 10  # Local variable
    print(x)

my_function()

# Global variables are accessible throughout the entire program:
x = 10  # Global variable

def my_global_function():
    global x  # Access the global variable
    x += 5
    print(x)

my_global_function()
print(x)  # Prints the modified global variable


# Data Types

# 4. Strings:
# Strings are sequences of characters enclosed in single (' ') or double (" ") quotes.
name = "Alice"
greeting = 'Hello, ' + name
print(greeting)

# You can also use string methods for formatting:
text = "hello world"
text_upper = text.upper()  # Convert to uppercase
print(text_upper)

# 5. Integers:
# Integers are whole numbers. Python supports basic arithmetic operations.
a = 5
b = 2
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division

# 6. Floats:
# Floats are numbers with a decimal point. Sometimes precision issues may occur.
c = 0.1 + 0.2
print(c)  # Result: 0.30000000000000004

# Handling precision issues by rounding the result:
rounded_c = round(c, 2)
print(f"Rounded value: {rounded_c}")

# Operators

# 7. Arithmetic Operators
# Used for mathematical operations:
x = 10
y = 5
print(x + y)  # Addition
print(x * y)  # Multiplication

# 8. Assignment Operators
# Assign values to variables:
x = 10
x += 5  # Increment x by 5
print(x)

# 9. Comparison Operators
# Compare values:
a = 5
b = 10
print(a == b)  # False
print(a < b)   # True

# 10. Logical Operators
# Combine conditional statements:
x = 5
print(x > 3 and x < 10)  # True
print(not(x < 10))       # False


# Lab Exercise

# Create a simple program that performs arithmetic operations and manipulates variables

# Variable Declaration:
a = 15
b = 12
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division

# Type Casting:
c = a // b  # Integer division
print(f"c (int) = {c}")
c = float(c)  # Convert to float
print(f"c (float) = {c}")

# String Manipulation:
message = "The result of a divided by b is:"
result = message + " " + str(c)
print(result)

# Comparison Operators:
print(a > b)  # True
print(a == b)  # False
