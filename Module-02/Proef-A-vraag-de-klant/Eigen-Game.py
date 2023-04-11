#jowad al fartousy

Fireinfo = ("""
===============================================
Firetype Pokémon are effective against Bug-, 
Grass-, Ice-, and Steel-type Pokémon, while
Fire-type Pokémon are weak to Ground-, Rock-, 
and Water-type Pokémon.
===============================================
""")
Grassinfo = ("""
================================================
Grasstype Pokémon are effective against water,-
ground and rock type Pokémon. But they are 
weaker to Bug-, Fire-, Flying-, Grass-, Poison-,
Dragon-, and Steel-type Pokémon.
================================================
""")
Waterinfo = ("""
================================================
Watertype Pokémon are super-effective against 
Fire-, Ground-, and Rock-type Pokémon, 
while Water-type Pokémon are weak to Electric- 
and Grass-type Pokémon.
================================================
""")

Start = print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"Hello! Sorry to keep you waiting! Welcome to the world of Pokémon!
My name is Oak. People call me the Pokémon Professor. This world is 
inhabited by creatures that we call Pokémon.People and Pokémon live 
together by supporting each other. Some people play with Pokémon, 
some battle with them. But we don't know everything about Pokémon yet. 
There are still many mysteries to solve. That's why I study Pokémon 
every day.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")

Player = input("Now, what did you say your name was? ")
Fire = "Torchic"
Grass = "Snivy"
Water = "Froakie"
start2 = print(f"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Are you ready {Player}? Your very own Pokémon story is about to unfold. 
You'll face fun times and tough challenges. A world of dreams and
adventures with Pokémon awaits! Let's go! You get to choose your own
starter Pokémon! Making this choise is important for your adventures 
to come, so choose wisely! There 3 starters Pokémon to choose from.
{Fire} the firetype Pokémon.
{Grass} the grasstype Pokémon.
{Water} the watertype Pokémon.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
question1 = input(f"Would you like to know more information about a starters type?,{Player} y/n: ")
if question1 == "y":
    question2 = input("Which starter would you like more information about? fire, grass, water: ")
    if question2 == "fire":
        print(f"{Fireinfo}")
    elif question2 == "grass":
        print(f"{Grassinfo}")
    else:
        print(f"{Waterinfo}")

#Pokemon choice
Areyousure = False
while Areyousure == "y":
    try:
        Playerpokemon = int(input("Which Starter would you like to choose? 1)fire, 2)grass, 3)water: "))
    except ValueError:
        print("""
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        This is not a choice.
        Choose from the choises given.
        Write the number for the type.
        anwser "n" for the next question!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """)
    Areyousure = input("Are you sure with your choice? y/n ")

if Playerpokemon == 1:
    print(f"""
    +++++++++++++++++++++++++++++
    interesting you choose {Fire}
    +++++++++++++++++++++++++++++
    """)
elif Playerpokemon == 2:
    print(f"""
    +++++++++++++++++++++++++++++
    interesting you choose {Grass}
    +++++++++++++++++++++++++++++
    """)
elif Playerpokemon == 3:
    print(f"""
    +++++++++++++++++++++++++++++
    interesting you choose {Water}
    +++++++++++++++++++++++++++++
    """)

mission = print(f"""
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
Your main goal is reaching the gymleader in time and defeating him.
if you fail to reach him or fail to defeat him you will lose. Choose
your routes and choices carefully.
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
""")
#Route choice

Routechoise = int(input("which route would you like to take? route 1,2,3 "))
if Routechoise == 1:
    print("""
    ________________________________________________________________
    You took route 1, you found and caught more pokemon on route 1.
    On your way to the gym you have encountered a trainer that wants
    to battle you.
    ________________________________________________________________
    """)
elif Routechoise == 2:
    print("""
    ________________________________________________________________
    You took route 2, you found and caught more pokemon on route 2.
    On your way to the gym you have encountered a trainer that wants
    to battle you.
    ________________________________________________________________
    """)
else:
    print("""
    ________________________________________________________________
    You took route 3, you found and caught more pokemon on route 3.
    On your way to the gym you have encountered a trainer that wants
    to battle you.
    ________________________________________________________________
    """)
    
#Routes

if Routechoise == 1:
    Fight1_solve1 = int(input("Solve this equation to win the fight, What is 125*5?: "))
    if Fight1_solve1 == 625 and Playerpokemon == 1:
        hiddenroute1 = int(input("""
        ================================================
        You have won the first battle and your fire type
        found a shortcut around the second battle.
        Which route do you want to take route 10 or 11?
        ================================================
        : """))
        if hiddenroute1 == 10:
            GymleaderQ1H = int(input("""
                ######################################################
                You have found the gym and challanged the gymleader.
                If you solve the next aquations you will win the fight.
                What is 10*12/4? 
                ######################################################
                : """))
            if GymleaderQ1H == 30:
                GymleaderQ2H = int(input("""
                ################################
                You defeated 1 out of 3 pokemon.
                Solve the next one to defaut 
                the second pokemon. Whats
                9/3*10+150?
                ################################
                : """))
                if GymleaderQ2H == 180:
                    GymleaderQ3H = int(input("""
                    ######################################
                    You have defeated 2 out of my 3
                    pokemon. You wont be able to defeat
                    my Last pokemon he its the undefeated
                    Hitmonlee!!!! Solve the last aquation 
                    to defeat the last pokemon and win 
                    the gym battle. Whats 123+321-(10*10)
                    ######################################
                    : """))
                    if GymleaderQ3H == 444:
                        print("""
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        congratulations you have defeated the gym leader and won the game.
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        """)
                    else:
                        print("""
                        ================================================
                        Your pokemon got defeated and you lost the game!
                        ================================================
                        """)
                else:
                    print("""
                    ================================================
                    Your pokemon got defeated and you lost the game!
                    ================================================
                    """)
            else:
                print("""
                ================================================
                Your pokemon got defeated and you lost the game!
                ================================================
                """)
        else:
            Mewtwo = int(input("""
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            You took route 11 and encountered The legendary pokemon mewtwo.
            Mewtwo attacks you. Solve this aquation to counter his attack.
            9*9-80
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            : """))     
            if Mewtwo == 1:
                print("""
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                You have countered the attack. Mewtwo took off leaving your pokemon wounded.
                You lost the game because you pokemon cant fight the gymleader anymore.
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """)
            else:
                print("""
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                Your pokemon got attack. Mewtwo took off leaving your pokemon wounded.
                You lost the game because you pokemon cant fight the gymleader anymore.
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """)
    else:
        Fight2_solve1 = int(input("""you won the first battle. Solve this second equation to win the fight second battle, What is 999/11?: """))
        if Fight2_solve1 == 90:
            Routechoise = int(input("You won both fights and can continue. Which route do you want to take route 10 or 11?: "))
        else:
            print("""
            ================================================
            Your pokemon got defeated and you lost the game!
            ================================================
            """)
            if Routechoise == 10:
                GymleaderQ1 = int(input("""
                ######################################################
                You have found the gym and challanged the gymleader.
                If you solve the next aquations you will win the fight.
                What is 10*12/4? 
                #####################################################
                : """))
                if GymleaderQ1 == 30:
                    GymleaderQ2 = int(input("""
                    ################################
                    You defeated 1 out of 3 pokemon.
                    Solve the next one to defaut 
                    the second pokemon. Whats
                    9/3*10+150?
                    ################################
                    : """))
                    if  GymleaderQ2 == 180:
                        GymleaderQ3 = int(input("""
                        ######################################
                        You have defeated 2 out of my 3
                        pokemon. You wont be able to defeat
                        my Last pokemon he its the undefeated
                        Hitmonlee!!!! Solve the last aquation 
                        to defeat the last pokemon and win 
                        the gym battle. Whats 123+321-(10*10)
                        ######################################
                        : """))
                        if GymleaderQ3 == 444 and Playerpokemon == 2:
                            print("""
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            congratulations you have defeated the gym leader and won the game.
                            !You have unlock the hidden achievement grass trainer because you 
                            won the game using a grass type and making the right choises!
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            """)
                        elif GymleaderQ3 == 444:
                            print("""
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            congratulations you have defeated the gym leader and won the game!
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            """)
                        else:
                            print("""
                            ================================================
                            Your pokemon got defeated and you lost the game!
                            ================================================
                            """)
                    else:
                        print("""
                        ================================================
                        Your pokemon got defeated and you lost the game!
                        ================================================
                        """)
                else:
                    print("""
                    ================================================
                    Your pokemon got defeated and you lost the game!
                    ================================================
                    """)
            else:
                print("""
                ================================================
                Your pokemon got defeated and you lost the game!
                ================================================
                """)  
elif Routechoise == 2:
    Fight1_solve1 = int(input("Solve this equation to win the fight, What is 125*5?: "))
    if Fight1_solve1 == 625 and Playerpokemon == 2:
        hiddenroute1 = int(input("""
        ================================================
        You have won the first battle and your fire type
        found a shortcut around the second battle.
        Which route do you want to take route 10 or 12?
        ================================================
        : """))
        if hiddenroute1 == 10:
            GymleaderQ1H = int(input("""
                ######################################################
                You have found the gym and challanged the gymleader.
                If you solve the next aquations you will win the fight.
                What is 10*12/4? 
                ######################################################
                : """))
            if GymleaderQ1H == 30:
                GymleaderQ2H = int(input("""
                ################################
                You defeated 1 out of 3 pokemon.
                Solve the next one to defaut 
                the second pokemon. Whats
                9/3*10+150?
                ################################
                : """))
                if GymleaderQ2H == 180:
                    GymleaderQ3H = int(input("""
                    ######################################
                    You have defeated 2 out of my 3
                    pokemon. You wont be able to defeat
                    my Last pokemon he its the undefeated
                    Hitmonlee!!!! Solve the last aquation 
                    to defeat the last pokemon and win 
                    the gym battle. Whats 123+321-(10*10)
                    ######################################
                    : """))
                    if GymleaderQ3H == 444:
                        print("""
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        congratulations you have defeated the gym leader and won the game.
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        """)
                    else:
                        print("""
                        ================================================
                        Your pokemon got defeated and you lost the game!
                        ================================================
                        """)
                else:
                    print("""
                    ================================================
                    Your pokemon got defeated and you lost the game!
                    ================================================
                    """)
            else:
                print("""
                ================================================
                Your pokemon got defeated and you lost the game!
                ================================================
                """)
        else:
            Rival = int(input("""
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            You took route 11 and encountered your rival in a cave. your
            rival challanges you. Solve this aquation to counter his attack.
            9*9-80
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            : """))     
            if Rival == 1:
                print("""
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                You've countered the attack of your rival and defeated his pokemon. The fight
                caused the cave entrance to cave in and locking you up inside. You couldnt 
                make it to the gymleader and lost the game
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """)
            else:
                print("""
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                Your pokemon got attack by your rival leaving your pokemon wounded.
                You lost the game because you pokemon cant fight the gymleader anymore.
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """)
    else:
        Fight2_solve1 = int(input("""you won the first battle. Solve this second equation to win the fight second battle, What is 999/11?: """))
        if Fight2_solve1 == 90:
            Routechoise = int(input("You won both fights and can continue. Which route do you want to take route 10 or 11?: "))
        else:
            print("""
            ================================================
            Your pokemon got defeated and you lost the game!
            ================================================
            """)
            if Routechoise == 10:
                GymleaderQ1 = int(input("""
                ######################################################
                You have found the gym and challanged the gymleader.
                If you solve the next aquations you will win the fight.
                What is 10*12/4? 
                #####################################################
                : """))
                if GymleaderQ1 == 30:
                    GymleaderQ2 = int(input("""
                    ################################
                    You defeated 1 out of 3 pokemon.
                    Solve the next one to defaut 
                    the second pokemon. Whats
                    9/3*10+150?
                    ################################
                    : """))
                    if  GymleaderQ2 == 180:
                        GymleaderQ3 = int(input("""
                        ######################################
                        You have defeated 2 out of my 3
                        pokemon. You wont be able to defeat
                        my Last pokemon he its the undefeated
                        Hitmonlee!!!! Solve the last aquation 
                        to defeat the last pokemon and win 
                        the gym battle. Whats 123+321-(10*10)
                        ######################################
                        : """))
                        if GymleaderQ3 == 444 and Playerpokemon == 3:
                            print("""
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            congratulations you have defeated the gym leader and won the game.
                            !You have unlock the hidden achievement water trainer because you 
                            won the game using a water type and making the right choices!
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            """)
                        elif GymleaderQ3 == 444:
                            print("""
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            congratulations you have defeated the gym leader and won the game!
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            """)
                        else:
                            print("""
                            ================================================
                            Your pokemon got defeated and you lost the game!
                            ================================================
                            """)
                    else:
                        print("""
                        ================================================
                        Your pokemon got defeated and you lost the game!
                        ================================================
                        """)
                else:
                    print("""
                    ================================================
                    Your pokemon got defeated and you lost the game!
                    ================================================
                    """)
            else:
                print("""
                ================================================
                Your pokemon got defeated and you lost the game!
                ================================================
                """)  
elif Routechoise == 3:
    Fight1_solve1 = int(input("Solve this equation to win the fight, What is 125*5?: "))
    if Fight1_solve1 == 625 and Playerpokemon == 3:
        hiddenroute1 = int(input("""
        ================================================
        You have won the first battle and your fire type
        found a shortcut around the second battle.
        Which route do you want to take route 10 or 13?
        ================================================
        : """))
        if hiddenroute1 == 10:
            GymleaderQ1H = int(input("""
                ######################################################
                You have found the gym and challanged the gymleader.
                If you solve the next aquations you will win the fight.
                What is 10*12/4? 
                ######################################################
                : """))
            if GymleaderQ1H == 30:
                GymleaderQ2H = int(input("""
                ################################
                You defeated 1 out of 3 pokemon.
                Solve the next one to defaut 
                the second pokemon. Whats
                9/3*10+150?
                ################################
                : """))
                if GymleaderQ2H == 180:
                    GymleaderQ3H = int(input("""
                    ######################################
                    You have defeated 2 out of my 3
                    pokemon. You wont be able to defeat
                    my Last pokemon he its the undefeated
                    Hitmonlee!!!! Solve the last aquation 
                    to defeat the last pokemon and win 
                    the gym battle. Whats 123+321-(10*10)
                    ######################################
                    : """))
                    if GymleaderQ3H == 444:
                        print("""
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        congratulations you have defeated the gym leader and won the game.
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        """)
                    else:
                        print("""
                        ================================================
                        Your pokemon got defeated and you lost the game!
                        ================================================
                        """)
                else:
                    print("""
                    ================================================
                    Your pokemon got defeated and you lost the game!
                    ================================================
                    """)
            else:
                print("""
                ================================================
                Your pokemon got defeated and you lost the game!
                ================================================
                """)
        else:
            Galactic = int(input("""
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                You took route 13 and encountered team galactic. Team galactics
                runts attack your pokemon. Solve this aquation to counter their
                attack. 9*9-80
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                : """))     
            if Galactic == 1:
                print("""
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                You defeated team galactic, but they summoned giritina who teleported
                you and your pokemon to another dimention. You lost the game because 
                you pokemon cant fight the gymleader anymore.
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """)
            else:
                print("""
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                Team galactic summoned giritina who teleported you and your pokemon 
                to another dimention. You lost the game because you pokemon cant 
                fight the gymleader anymore.
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                """)
    else:
        Fight2_solve1 = int(input("""you won the first battle. Solve this second equation to win the fight second battle, What is 999/11?: """))
        if Fight2_solve1 == 90:
            Routechoise = int(input("You won both fights and can continue. Which route do you want to take route 10 or 11?: "))
        else:
            print("""
            ================================================
            Your pokemon got defeated and you lost the game!
            ================================================
            """)
            if Routechoise == 10:
                GymleaderQ1 = int(input("""
                ######################################################
                You have found the gym and challanged the gymleader.
                If you solve the next aquations you will win the fight.
                What is 10*12/4? 
                #####################################################
                : """))
                if GymleaderQ1 == 30:
                    GymleaderQ2 = int(input("""
                    ################################
                    You defeated 1 out of 3 pokemon.
                    Solve the next one to defaut 
                    the second pokemon. Whats
                    9/3*10+150?
                    ################################
                    : """))
                    if  GymleaderQ2 == 180:
                        GymleaderQ3 = int(input("""
                        ######################################
                        You have defeated 2 out of my 3
                        pokemon. You wont be able to defeat
                        my Last pokemon he its the undefeated
                        Hitmonlee!!!! Solve the last aquation 
                        to defeat the last pokemon and win 
                        the gym battle. Whats 123+321-(10*10)
                        ######################################
                        : """))
                        if GymleaderQ3 == 444 and Playerpokemon == 1:
                            print("""
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            congratulations you have defeated the gym leader and won the game.
                            !You have unlock the hidden achievement fire trainer because you 
                            won the game using a fire type and making the right choices!
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            """)
                        elif GymleaderQ3 == 444:
                            print("""
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            congratulations you have defeated the gym leader and won the game!
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            """)
                        else:
                            print("""
                            ================================================
                            Your pokemon got defeated and you lost the game!
                            ================================================
                            """)
                    else:
                        print("""
                        ================================================
                        Your pokemon got defeated and you lost the game!
                        ================================================
                        """)
                else:
                    print("""
                    ================================================
                    Your pokemon got defeated and you lost the game!
                    ================================================
                    """)
            else:
                print("""
                ================================================
                Your pokemon got defeated and you lost the game!
                ================================================
                """)
else:
    print("you're an idiot")