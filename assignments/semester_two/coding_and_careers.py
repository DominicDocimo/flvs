# Dominic Docimo
# 09/13/2022
# This program will simulate a rock paper scissors game

from random import choice

active = True
kill = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while active:
    user = input("Rock, Paper, or Scissors? (q to quit)")
    user = user.lower()
    computer = choice(["rock", "paper", "scissors"])

    if user == "q":
        active = False

    elif user not in kill.keys():
        print("Invalid Input")

    elif user == computer:
        print("Tie!")

    else:
        if kill[user] == computer:
            print("You win!")
        else:
            print("You lose!")

    print(user + " vs " + computer)
print("Thanks for playing!")
