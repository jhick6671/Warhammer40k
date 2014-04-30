import random
class Dice():
    """ The game WH40k is a D6 base game. This class will simulate dice rolling."""

    def __init__(self, dice, hit, wound, save, top=6,) :
        self.dice = [random.randint(1, top) for die in range(dice)]
        self.hit = hit
        self.save = save
        self.wound = wound
        self.top = top

    def ToHit(self):
        """ This will compare the number of dice rolled to the user input for what is needed to hit. The number of hits
        dealt is the number greater than or equal to the user input value for what they need to hit with."""
        hits = len([die for die in self.dice if die >= self.hit])
        self.dice = [random.randint(1, self.top) for die in range(hits)]
        return hits

    def ToWound(self):
        """ This will compare the number of dice that hit to the user input for what is needed to wound. The number of
        wounds dealt needs to be greater than or equal to the user inputted value for what they need to wound with."""
        wounds = len([die for die in self.dice if die >= self.wound])
        self.dice = [random.randint(1, self.top) for die in range(wounds)]
        return wounds

    def WoundsDealt(self):
        """ This is to compare the number of wounds to the inputted save value. The output should be the number
        of wounds not saved, meaning the defending unit is taking this amount of wounds"""
        saved = len([die for die in self.dice if die >= self.save])
        return len(self.dice) - saved

def statistics(runtime = 100):
    """ In this section we want the program to run X amount of times and produce statistics from the results. To keep it
    simple we just want to see the maximum, minimum, and average for hit, wound and saved."""
    count = 0
    results = []
    while count < runtime:
        d = Dice(20,4,4,3)
        results.append((d.ToHit(), d.ToWound(), d.WoundsDealt()))
        count += 1

    print("The maximum number of hits:" + str(max([r[0] for r in results])))
    print("The minimum number of hits:" + str(min([r[0] for r in results])))
    print("The average number of hits:" + str(sum([r[0] for r in results])/len([r[0] for r in results])))
    print("The maximum number of wounds:" + str(max([r[1] for r in results])))
    print("The minimum number of wounds:" + str(min([r[1] for r in results])))
    print("The average number of wounds:" + str(sum([r[1] for r in results])/len([r[1] for r in results])))
    print("The maximum number of saves:" + str(max([r[2] for r in results])))
    print("The minimum number of saves:" + str(min([r[2] for r in results])))
    print("The average number of saves:" + str(sum([r[2] for r in results])/len([r[2] for r in results])))

statistics()