# Dominic Docimo
# 09/08/2022
# This program will control a turtle from user request

from random import choice
import turtle

colors = ["red", "blue", "green", "yellow"]
active = True

player = turtle.Turtle()
player.shape("turtle")
player.color(choice(colors))
player.speed(10)
player.pensize(10)

string = "~Turtle Control~\nSelect a command:\nW) Forward\nS) Backward\nA) Left\nD) Right\nR) Exit"

print(string)

while active:

    command = input("New option?")
    player.color(choice(colors))
    if command == "w":
        player.pendown()
        player.forward(100)
        player.penup()
        "Draw a line forward 100 pixels"

    elif command == "d":
        player.pendown()
        player.right(90)
        player.forward(100)
        player.penup()

    elif command == "a":
        player.pendown()
        player.left(90)
        player.forward(100)
        player.penup()

    elif command == "s":
        player.pendown()
        player.right(180)
        player.forward(100)
        player.penup()

    elif command == "r":
        print("Thanks for playing!")
        active = False
