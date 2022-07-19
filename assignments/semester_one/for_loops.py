# Dominic Docimo
# 7/8/2022
# This program will use a for loop to print a square

import turtle


def main():
    print("This is a square")
    colors = ["red", "blue", "green", "yellow"]
    x = turtle.Turtle()
    x.speed(10)

    for i in range(len(colors)):
        x.color(colors[i])
        x.forward(100)
        x.left(90)


main()
