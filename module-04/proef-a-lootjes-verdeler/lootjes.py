#jowad al fartousy
import random
lijst_van_namen = []
lijst_shuffle = []
lootjes = {}
namen = True
shuffling = False
while namen:
    namen_invoer = input("Welke naam wil je toevoegen?: ")
    if namen_invoer not in lijst_van_namen:
        lijst_van_namen.append(namen_invoer)
        lijst_shuffle.append(namen_invoer)
        namen_opnieuw = input("Wil je nog een naam toevoegen? ja/nee: ")
        if namen_opnieuw == "ja":
                namen = True
        else:
            if len(lijst_van_namen) < 3:
                print("Moet minimaal 3 namen invullen!")
            else:
                namen = False
                shuffling = True
    else:
        print("Die naam is al gegeven!")

while shuffling: 
    random.shuffle(lijst_shuffle)
    shuffling = False
    for x in range(len(lijst_van_namen)):
        if lijst_van_namen[x] != lijst_shuffle[x]:
            lootjes[lijst_van_namen[x]] = lijst_shuffle[x]
        else:
            shuffling = True    

for x, y in lootjes.items():
    print(f"{y.capitalize()} heeft {x.capitalize()}")