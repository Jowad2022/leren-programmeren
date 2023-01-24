#jowad al fartousy
boodschappenlijst = {}
loop = True

while loop:
    vraag_1 = input("Wat wil je toevoegen aan je lijst?: ").lower()
    vraag_2 = int(input(f"Hoeveel {vraag_1} wil je?: "))
    if vraag_1 in boodschappenlijst.keys():
        boodschappenlijst.update({vraag_1: vraag_2})
    boodschappenlijst[vraag_1] = vraag_2
    opnieuw = input("Wil je nog iets toevoegen?: ").lower()
    if opnieuw == "nee":
        loop = False
    else:
        loop = True

print("-[BOODSCHAPPENLIJST]-")
for x, y in boodschappenlijst.items():
    print(f"{y}x {x.capitalize()}")

print("---------------------")