# Dominic Docimo
# 9/13/2022
# This program will evaluate user input

print("Welcome to the DMV. I have some questions for you:")

age = int(input("How old are you? "))
suspended = input("Is your license currently suspended? (y/n) ")
safety_course = input("Have you taken a driver safety course? (y/n) ")
conditions = [True if age >= 16 else False, True if suspended == "n" else False,
              True if safety_course == "y" else False]

if all(conditions):
    print("You are eligible for a license.")

elif any(conditions):
    print("You are not eligible for a license due to a few requirements not being met:")
    print("Age Requirement: " + str(conditions[0]) + " License Suspended: " + str(conditions[1]) +
          " Driver Safety Course: " + str(conditions[2]))

else:
    print("You are not eligible for a license due to meeting none of the requirements.")
