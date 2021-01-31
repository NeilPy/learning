from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        if roll == 6:
            print("You lose")
        else:
            print("You luck")
        return roll


sides_6 = Die()
print(sides_6.roll_die())
print(sides_6.roll_die())
print(sides_6.roll_die())
print(sides_6.roll_die())
print(sides_6.roll_die())
sides_10 = Die(10)
print(sides_10.roll_die())
print(sides_10.roll_die())
print(sides_10.roll_die())
print(sides_10.roll_die())
print(sides_10.roll_die())
sides_20 = Die(20)
print(sides_20.roll_die())
print(sides_20.roll_die())
print(sides_20.roll_die())
print(sides_20.roll_die())
print(sides_20.roll_die())
