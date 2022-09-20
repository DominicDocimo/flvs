# Dominic Docimo
# 09/09/2022
# This program will convert inches to feet and kilometers

values = [5, 7, 3, 2, 18]


def inches_to_feet(inches: float) -> float:
    feet = inches / 12
    return feet


for item in values:
    print(str(item) + " inches is " + str(inches_to_feet(float(item))) + " feet")
