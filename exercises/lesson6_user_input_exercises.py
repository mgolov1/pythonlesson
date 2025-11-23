# 1. Greeting
# Create a simple program that asks for users name and responds with personalized greeting.

age = input("Enter your age: ")
print("You are " + age + " years old")

# 2. Echo Machine
# Create a simple program that prompts the user to type something and then repeat it back exactly as entered.

user_input = input("Say something: ")
print(user_input)

# 3. Favorite Color
# Create a program that inquires about the users favorite color and responds with the comment about that color.

color = input("What's your favorite color: ")
print(f"{color} is a great color! It reminds me of {color} skies.")

# Multiple Inputs
# 4. Create a program that gathers the users name, age, and hometown, then crafts a summary sentence using this information

name = input("Enter your name: ")
age = input("Enter your age: ")
hometown = input("Enter your hometown: ")
print(f"{name} is {age} years old and is from {hometown}")

# 5. Pet Description
# Write a program that asks for a pets name, species, and age, then generates a sentence describing the pet.

pet_name = input("Enter your pets name: ")
pet_species = input("What kind of animal is your pet: ")
pet_age = input("How old is your pet? ")
print(f"{pet_name} is a {pet_species} that is {pet_age} years old")

# 6. Travel Planner
# Write a program that requests a destination, mode of transport, and duration of stay, then prints a brief travel plan.

destination = input("Where do you want to go? ")
transport = input("How will you get there? ")
duration = input("How long will you stay there? ")
print(f"You will travel to {destination} by {transport} and stay there for {duration}. Have a great trip!")

# Converting Input to Integers
# 7. Create a program that asks for the users name, converts it into an integer, then calculates and prints their age in 'dog years'

human_age = int(input("Enter your age: "))
dog_age = human_age * 7
print(f"You are {dog_age} years old in dog years!")

# 8. Simple Calculator
# Create a program that prompts for two numbers and operation (+, -, *, /) then it performs the calculation and displays the results

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter an operation to perform ( +, -, *, / ): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"Result: {result}")

# 9. Days to Hours
# Develop a program that asks for a number of days, converts it into an integer, then calculates and prints the equivalent number in hours.

days = int(input("Enter number of days: "))
hours = days * 24
print(f"{days} is equal to {hours} hours")

# 10. Mad Libs
# Create a simple Mad Libs game. Ask the user for an adjective, a noun, and a verb, then use these inputs to complete a pre-written sentence.

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
print(f"{adjective} {noun} {verb} over the lazy dog.")