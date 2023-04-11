#jowad al fartousy
import random
from time import sleep
def dice_roll():
    return random.randint(1,6)


print("""
===========================================================================
Welcome to the golden rush dungeon.
in this dungeon you'll get to choose your own paths to complete the game.
everypath has its own monsters. every monster you defeat wil drop gold.
if you survive the dungeon you'll be able to leave with all the gold that
you earnd.
===========================================================================
""")
sleep(1)
print(""" 
=======================================================================================
you have been given 2 lives. if you lose all of your lives you lose the game.
you'll encounter some monster in the dungeon and you'll get to choose. fight or run
=======================================================================================
""")
sleep(1)
print(""" 
=======================================================================================
fight them of to run away from them. if you decide to fight a dice will be roled.
the number of the dice is the damage you will deal to the monster.
all monsters have 3 health points. if you decide to run a dice will be rolled
========================================================================================
""")
sleep(1)
print(""" 
=======================================================================================
if the number is odds a life will be lost and you can choose the next tunnel. 
if the number is even your life will be spared and get to choose the next tunnel
========================================================================================
""")
sleep(1)

monster_list = [
    ("Goblins"),
    ("Wolfs"),
    ("undead"),
    ("imps"),
    ("skeletons")
    ]
events_list = [
    ("you have encounterd some monsters"),
    ("you have encounterd nothing"),
    ("you have found a treasure chest")
    ]
for rounds in range(5):
    tunnels = [1,2,3]
    Lives = 3
    gold = 0
    while rounds < 5:
        if rounds == 5:
            print(f"""
            good job. you have defeated the dungeon.
            You have collected {gold} gold
            """)
            rounds == 6
        elif Lives < 1:
            print(f"""
            you have lost all of your lives
            ===================
            =====Game over=====
            ===================
            """)
            rounds == 6
        try:
            tunnel_choice = int(input("which tunnel do you choose to enter? 1/2/3: "))
            if tunnel_choice  in tunnels: # fight no treasure
                # choice = False
                print(f"you choose tunnel: {tunnel_choice}")
                sleep(1)
                events = random.randint(0,2)
                encounter = random.randint(1,4)
                encounter = (monster_list[encounter])
                print(events_list[events])
            else:
                print("That's not a choice")
        except ValueError:
            print("Choose one of the given options please.")
        event_round = True
        while event_round:
            try:
                if events == 0:
                    choice_1 = int(input("do you want to run or fight? 1(Fight),2(run): "))
                    run_fight = [1,2]
                    odds = [1,3,5]
                    even = [2,4,6]
                    if choice_1 in run_fight:
                        print("get ready")
                        sleep(1)
                        if choice_1 == 1:
                            print(f"""
                            The {encounter} have 3 health.
                            rolled the dice....
                            """)
                            roll_fight = dice_roll()
                            sleep(2)
                            print(f"you rolled {roll_fight}")
                            if roll_fight >= 2:
                                gold_gained =  random.randint(5,20)
                                gold = gold + gold_gained
                                Lives = Lives + 1
                                print(f"""
                                    you have defeated the {encounter} and you have gained 1 live and {gold_gained} gold.
                                    your lives left = {Lives}
                                    total gold = {gold}
                                    """)
                                event_round = False
                            else:
                                Lives = Lives - 1
                                print(f"""
                                You lost the fight and one of your lifes.
                                Lives left = {Lives}
                                total gold = {gold}
                                """)
                                event_round = False
                                if Lives < 1:
                                    print(f"""
                                    you have lost all of your lives
                                    ===================
                                    =====Game over=====
                                    ===================
                                    """)
                        elif choice_1 == 2:
                            print(f"""
                            You're trying to avoid the {encounter}.
                            you rolled the dice. odds = -1 live / even = 0 lives lost.
                            """)
                            roll_run = dice_roll()
                            sleep(2)
                            print(f"you rolled {roll_run}")
                            sleep(1)
                            if roll_run in odds:
                                Lives = Lives - 1
                                print(f"""
                                you ran from the {encounter} but got hurt and lost a live.
                                Lives left = {Lives}
                                """)
                                event_round = False
                            else:
                                print(f"you succesfully ran away from the {encounter} without losing a life")
                                event_round = False
                    else:
                        print("That's not a choice")
                elif events == 2:
                    gold = gold + 10
                    print(f"""
                        you have gained 10 gold
                        total gold = {gold}
                        """)
                    event_round = False
                elif events == 1:
                    event_round = False
            except ValueError:
                print("Choose one of the given options please.")
