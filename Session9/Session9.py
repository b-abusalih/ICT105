#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Python Tutorial: Error Handling, Debugging, and Modular Programming

# ------------------------------------------
# 1. Reading from a File
    # Using pathlib to work with file paths and read file contents.

from pathlib import Path

# Create a Path object representing the file 'pi_digits.txt'
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()  # Read the entire file and remove trailing newline
print(contents)  # Output: Content of the file, such as digits of pi


# *Note. The lstrip(s) (left strip) function removes leading whitespace (on the left) in the string. The rstrip(s) (right strip) function removes the trailing whitespace (on the right).*

# In[32]:


# 2. Relative and Absolute File Paths
# Use relative paths for portability and absolute paths for fixed locations.

# Relative file path
relative_path = Path('text_files/pi_digits.txt')

# Absolute file path (modify as per your system)
absolute_path = Path('C:/Users/user2/OneDrive - Curtin/UJ/UJ/Teaching/Stanley College/ICT105/Week 9/text_files/pi_digits.txt')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[33]:


# 3. Accessing and Modifying File Contents
# Splitting file content into lines for easy access and manipulation.

path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()  # Split into individual lines

print(type(lines))

for line in lines:
    print(line)  # Each line of 'pi_digits.txt' is printed separately

# Concatenate lines into a single string
pi_string = ''.join(line.lstrip() for line in lines)
print(f"Pi: {pi_string}")
print(f"Length of pi string: {len(pi_string)}")


# In[34]:


from pathlib import Path

# Create a Path object representing the file 'pi_million_digits.txt'
path = Path('pi_million_digits.txt')

# Read the entire contents of the file into a string
contents = path.read_text()

# Split the string into a list of lines
lines = contents.splitlines()

# Initialize a variable to hold the digits of pi
pi_string = ''

# Iterate through each line and add it to the pi_string
for line in lines:
    pi_string += line.lstrip()

# Print the first 50 decimal places and the length of the string
print(f"{pi_string[:52]}...")
print(len(pi_string))


# In[35]:


# ------------------------------------------
# 4. Writing to a File
# Save program output, or data, to files using write_text.

from pathlib import Path

# Define the contents of the file with multiple lines
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

# Create a Path object representing the file 'programming.txt'
path = Path('programming.txt')

# Write the contents to the file
path.write_text(contents)



# In[36]:


# ------------------------------------------
# 5. Exception Handling: Catching ZeroDivisionError
# Using try-except blocks to prevent program crashes.

#print(5 / 0)

try:
    result = 5 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


# In[ ]:





# In[37]:


# ------------------------------------------
# 6. Exception Handling with User Input
# Handling exceptions while prompting user input.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Please enter valid numbers.")
    except Exception:
        pass #do nothing
    else:
        print(answer)


# In[ ]:





# In[39]:


# ------------------------------------------
# 7. Handling FileNotFoundError
# Gracefully handle missing file errors.

path = Path('alice2.txt')

#contents = path.read_text(encoding='utf-8')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")


# In[ ]:





# In[40]:


# ------------------------------------------
# 8. Working with Multiple Files
# Process multiple files while handling missing ones.

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)


# In[ ]:





# In[41]:


# ------------------------------------------
# 9. Failing Silently with pass
# Use pass in except blocks to ignore specific exceptions.

def count_words_silently(path):
    """Count words, but fail silently if file is missing."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

count_words_silently(Path('non_existent_file.txt'))


# In[ ]:





# In[42]:


# ------------------------------------------
# 10. Storing Data with JSON
# Save and load data using JSON, a popular data format.

import json

# Saving data to JSON
numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
path.write_text(json.dumps(numbers))

# Loading data from JSON
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)


# In[ ]:





# In[43]:


# ------------------------------------------
# 11. Saving User Data
# Storing and retrieving user input for future sessions.

username = input("What is your name? ")
path = Path('username.json')
path.write_text(json.dumps(username))
print(f"We'll remember you when you come back, {username}!")

# Loading stored user data
path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
    print(f"We'll remember you when you come back, {username}!")


# In[ ]:





# In[44]:


# ------------------------------------------
# 12. Modularizing Code with Functions
# Refactor code into functions to improve readability and reusability.

def get_stored_username(path):
    """Retrieve stored username if available."""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None

def get_new_username(path):
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()


# In[ ]:




