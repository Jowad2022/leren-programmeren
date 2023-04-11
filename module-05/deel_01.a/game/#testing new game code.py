#testing new game code
import random
# from time import sleep
# monster_list = [
#     ("Goblins"),
#     ("Wolfs"),
#     ("undead"),
#     ("imps"),
#     ("skeletons")
#     ]
# randon_monster = random.randint(1,4)
# encounter = (monster_list[randon_monster])
# print(encounter)


def dice_roll():
    roll = random.randint(1,6)
    return roll

var = dice_roll()
print(var)
