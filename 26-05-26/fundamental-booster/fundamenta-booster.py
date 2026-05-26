import datetime

print("WElcome to the Interactive Personal Data Collector!")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
favourite_number = int(input("Enter your favourite number: "))

print("Thank you! Here is the information we collected:")

print("Name:", name, type(name), id(name))
print("Age:", age, type(age), id(age))
print("Height:", height, type(height), id(height))
print("Favourite Number:", favourite_number, type(favourite_number), id(favourite_number))

current_year = datetime.datetime.now().year

birth_year = current_year - age

print(f"Your birth year is approximately: {birth_year} (based on your age of {age})")

print("Thank you for using the Personal Data collector.")
print("Goodbye!!!")