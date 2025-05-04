# Variables and Data Types Practice
# Author: Saheer Azmi

# Variable Examples

# Integer (int)
age=67
print("age:",age)
print("Type of age:", type(age))

# Float (decimal number)
price = 99.99
print("Price:", price)
print("Type of price:", type(price))

# String (text)
name = "Saheer Azmi"
print("Name:", name)
print("Type of name:", type(name))

# Boolean (True or False)
is_student = True
print("Is Student:", is_student)
print("Type of is_student:", type(is_student))

# List (group of items, changeable)
fruits = ["apple", "banana", "mango"]
print("Fruits List:", fruits)
print("Type of fruits:", type(fruits))

# Tuple (group of items, not changeable)
colors = ("red", "green", "blue")
print("Colors Tuple:", colors)
print("Type of colors:", type(colors))

# Dictionary (key-value pairs)
student_info = {
    "name": "Saheer",
    "age": 21,
    "is_student": True
}
print("Student Info Dictionary:", student_info)
print("Type of student_info:", type(student_info))

# -------------------------------
# Variables, Data Types with Input Practice - Saheer Azmi

# Taking user inputs
name = input("Enter your name: ")
city = input("Enter your city: ")
favorite_food = input("Enter your favorite food: ")

# For numbers, we have to convert input to int or float
age = int(input("Enter your age: "))
number_of_books = int(input("How many books do you have? "))
height_in_meters = float(input("Enter your height in meters: "))
weight_in_kg = float(input("Enter your weight in kg: "))

# Boolean type from user (answer should be yes/no)
is_student_input = input("Are you a student? (yes/no): ")
is_student = True if is_student_input.lower() == "yes" else False

likes_reading_input = input("Do you like reading books? (yes/no): ")
likes_reading = True if likes_reading_input.lower() == "yes" else False

# Printing the collected information
print("\n----- Your Information -----")
print("Name:", name)
print("City:", city)
print("Favorite Food:", favorite_food)
print("Age:", age)
print("Number of Books:", number_of_books)
print("Height (meters):", height_in_meters)
print("Weight (kg):", weight_in_kg)
print("Is Student:", is_student)
print("Likes Reading:", likes_reading)