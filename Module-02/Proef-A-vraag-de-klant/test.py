while True:
    try:
        Playerpokemon = int(input("Which Starter would you like to choose? 1)fire, 2)grass, 3)water: "))
    except ValueError:
        print("""
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        This is not a choise.
        Choose from the choises given.
        Write the number for the type.
        anwser "n" for the next question!
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """)
    Areyousure = input("Are you sure with your choise? y/n ")
    if Areyousure == "y":
         break
