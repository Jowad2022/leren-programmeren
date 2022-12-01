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

print("""
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
print(f"""
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


while True:
    try:
        Playerpokemon = (input("Which Starter would you like to choose? fire,grass,water: "))
    except ValueError:
        print("""
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        This is not a choise.
        Choose from the choises given.
        Don't for get uppercase character.
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """)
    Areyousure = input("Are you sure with your choise? y/n ")
    if Areyousure == "y":
         break

if Playerpokemon == "fire":
    print(f"interesting you choose {Fire}")
elif Playerpokemon == "grass":
    print(f"interesting you choose {Grass}")
else:
    print(f"interesting you choose {Water}")

print("""
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
Your main goal is reaching the gymleader in time and defeating him.
if you fail to reach him or fail to defeat him you will lose. Choose
your routes and choises carefully.
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
 """)

Routechoise = input("which route would you like to take? route 1,2,3 ")
if Routechoise == "1":
    print("""
    ________________________________________________________________
    You took route 1, you found and caught more pokemon on route 1.
    On your way to the gym you have encountered a trainer that wants
    to battle you.
    ________________________________________________________________
    """)
elif Routechoise == "2":
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

if Routechoise == "1":
    Fight1_solve1 = int(input("Solve this equation to win the fight, What is 125*5?: "))
    if Fight1_solve1 == "625" and :
        print("You have won the first battle and fire type found a shortcut around the second battle.")
        Fight1_solve2 = int(input("""you won the first battle. Solve this second equation to win the fight second battle, What is 125*5?: """))

       