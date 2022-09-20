from random import choice


class Superhero:
    def __init__(self, name="", strength_points=0):
        self.name = name
        self.strengthPts = strength_points
        self.primary_power = "flight"
        self.lore = "He saves people, flies, has speed, "
        self.has_cape = False

    def add_strength_points(self, points: int):
        self.strengthPts += points

    def change_primary_power(self, new_power: str):
        self.primary_power = new_power

    def fight_villain(self):
        result = choice([True, False])
        print("You " + {True: "won", False: "lost"}[result] + " the fight.")


superhero = Superhero("Superman", 100)
superhero.change_primary_power("Super Speed")

print(superhero.name + " has " + str(superhero.strengthPts) + " strength points. " + superhero.lore + " and " +
      {True: "has", False: "does not have"}[superhero.has_cape] + " a cape.")

points = int(input("How many strength points do you want to add? "))
superhero.add_strength_points(points)
fight = input("Do you want to fight the villain? (y/n) ")

if fight == "y":
    superhero.fight_villain()
else:
    print("You ran away from the fight.")

