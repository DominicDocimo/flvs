# Dominic Docimo
# 6/26/22
# This program will use the math module

from math import pow


def main():
    print("Dave wants to create a program that can determine the volume and surface area of any sphere, given the name "
          "and radius.")

    name = input("What is the name of the object?")
    radius = float(input("What is the radius?"))

    print("The volume of " + name + " is " + str((4.0/3.0) * 3.14 * pow(radius, 3)) + " and the surface area is " + str(4 * 3.14 * pow(radius, 2)))


main()
