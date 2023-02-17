#jowad al fartousy
names = {}
def ask():
    stop = True
    while stop:
        naam = input("Wat is de naam?: ")
        leeftijd = int(input(f"Wat de leeftijd van {naam}: "))
        opnieuw = input("Toets enter om door te gaan of stop om te printen: ")
        if opnieuw == "stop" or leeftijd == "stop":
            stop = False
        elif naam not in names.keys():
            names[naam] = leeftijd
        else:
            print("Die naam heb ik al")

ask()
for x, y in names.items():
    print(f"{x.capitalize()} is {y} jaar")



