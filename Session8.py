# Python Tutorial: Classes and Methods

# ------------------------------------------
# 1. Defining and Using a Simple Class
# A class in Python is a blueprint for creating objects (instances).
# Define a class to represent a simple object, like a dog.

class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Create an instance (object) of the Dog class
my_dog = Dog('Willie', 6)

# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name}.")  # Output: Willie's name
print(f"My dog is {my_dog.age} years old.")  # Output: 6 years old
my_dog.sit()  # Output: Willie is now sitting
my_dog.roll_over()  # Output: Willie rolled over

# ------------------------------------------
# 2. Creating Multiple Instances
# Each instance of a class has its own separate attributes and methods.

your_dog = Dog('Lucy', 3)

# Accessing attributes and calling methods on different instances
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# ------------------------------------------
# 3. Working with Attributes
# You can modify the attributes of an instance either directly or through methods.

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default attribute
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# Create an instance of the Car class
my_new_car = Car('Audi', 'A4', 2024)
print(my_new_car.get_descriptive_name())

# Modify the odometer attribute directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Use a method to update the odometer
my_new_car.update_odometer(100)
my_new_car.read_odometer()

# Increment the odometer value
my_new_car.increment_odometer(50)
my_new_car.read_odometer()

# ------------------------------------------
# 4. Inheritance
# Inheritance allows you to create a new class that inherits attributes and methods from another class.

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class, then initialize electric car-specific attributes."""
        super().__init__(make, model, year)
        self.battery_size = 40  # Attribute specific to electric cars
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    # Override a method from the parent class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

# Create an instance of the ElectricCar class
my_electric_car = ElectricCar('Tesla', 'Model S', 2024)
print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()
my_electric_car.fill_gas_tank()

# ------------------------------------------
# 5. Using Composition
# Instead of inheriting everything from a parent class, you can break down functionality into smaller classes.

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCarWithBattery(Car):
    """Models aspects of a car, specific to electric vehicles with a battery."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()  # Use composition: the electric car has a battery

# Create an instance of ElectricCarWithBattery
my_tesla = ElectricCarWithBattery('Tesla', 'Model X', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# ------------------------------------------
# 6. Importing Classes from Modules
# You can organize your classes in separate files (modules) and import them into other programs.

# For example, save the Car and ElectricCar classes in car.py, then import them like this:

# car.py (module)
# class Car: (as defined earlier)
# class ElectricCar: (as defined earlier)

# main_program.py
from car import Car, ElectricCar

my_audi = Car('Audi', 'Q5', 2024)
print(my_audi.get_descriptive_name())

my_leaf = ElectricCar('Nissan', 'Leaf', 2024)
print(my_leaf.get_descriptive_name())

# ------------------------------------------
# Lab Exercises
# ------------------------------------------
# 1. User Profile
class User:
    """A class to represent a user profile."""
    
    def __init__(self, first_name, last_name, age, location):
        """Initialize the user's profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")
    
    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0

# Create instances of the User class
user_1 = User('Alice', 'Smith', 30, 'New York')
user_2 = User('Bob', 'Johnson', 40, 'Los Angeles')

# Describe users and greet them
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

# Track login attempts
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"Login attempts after reset: {user_1.login_attempts}")

# ------------------------------------------
# 2. Restaurant
class Restaurant:
    """A class to represent a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print the restaurant's details."""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.restaurant_name} is now open!")
    
    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number
    
    def increment_number_served(self, number):
        """Increment the number of customers served."""
        self.number_served += number

# Create instances of the Restaurant class
restaurant = Restaurant('Pasta House', 'Italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Modify and display the number of customers served
restaurant.set_number_served(50)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(25)
print(f"Number served: {restaurant.number_served}")

# ------------------------------------------
# 3. Ice Cream Stand (Inheritance Example)
class IceCreamStand(Restaurant):
    """A class to represent an ice cream stand, inheriting from Restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        """Initialize attributes from the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
    
    def display_flavors(self):
        """Display the available ice cream flavors."""
        print(f"We have the following flavors available: {', '.join(self.flavors)}.")

# Create an instance of IceCreamStand
ice_cream_stand = IceCreamStand('Sweet Treats')
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
