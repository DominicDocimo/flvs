# Dominic Docimo
# 9/8/2022
# This program will allow a user to pick their favorite thing from a list

editors = ["pycharm", "visual studio code", "atom", "neovim", "sublime"]

user_favorite = input("What is your favorite editor?")
user_favorite = user_favorite.lower()

if user_favorite in editors:
    print("That's a good editor!")

elif user_favorite == "visual studio":
    print("You should quit programming.")

else:
    print("That's not in my favorites list.")

print("Here are my favorite:")
print("1) " + editors[0])
print("2) " + editors[1])
print("3) " + editors[2])
print("4) " + editors[3])
print("5) " + editors[4])
