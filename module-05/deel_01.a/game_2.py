#jowad al fartousy
import random
from time import sleep
def gold_count(gold):
    totaal = totaal + gold
    return totaal
gold = 0

def dice_roll(roll):
    roll = random.randint(1,6)
    return roll


print("""
===========================================================================
Welcome to the golden rush dungeon.
in this dungeon you'll get to choose your own paths to complete the game.
everypath has its own monsters. every monster you defeat wil drop gold.
if you survive the dungeon you'll be able to leave with all the gold that
you earnd.
===========================================================================
""")
sleep(10)
print(""" 
=======================================================================================
you have been given 2 lives. if you lose all of your lives you lose the game.
you'll encounter some monster in the dungeon and you'll get to choose. fight or run
=======================================================================================
""")
sleep(10)
print(""" 
=======================================================================================
if you decide to fight a dice will be roled.
the number of the dice is the damage you'll deal to the monster.
all monsters have between 2-4 health points. if you decide to run a dice will be rolled.
========================================================================================
""")
sleep(10)
print(""" 
=======================================================================================
if you decide to run a dice will be rolled.
if the number is odds a life will be lost and you get to choose the next tunnel. 
if the number is even your life will be spared and get to choose the next tunnel.
========================================================================================
""")
sleep(10)
choice = True
while choice:
    try:
        tunnel_choice = int(input("which door tunnel do you choose to enter? 1/2/3"))
        if tunnel_choice == 1: # fight no treasure
            choice = False
        elif tunnel_choice == 2: # fight and treasure
            choice = False
        elif tunnel_choice == 3: # only treasure
            choice = False
        else:
            print("That's not a choice")
    except ValueError:
        print("Choose one of the given options please.")

#first tunnel
    if tunnel_choice == 1:
        print("you have encounterd some goblins")
    elif tunnel_choice == 2:
        print("you have encounterd some goblins")
    elif tunnel_choice == 3:
        print("you have found a treasure chest")

# for x in range():
#     print()
