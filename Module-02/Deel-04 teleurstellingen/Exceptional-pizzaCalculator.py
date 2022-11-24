#Jowad al-fartousy, exceptional-pizzaCalculator

print("""=====Menu====
Small  € 5.95
meduim € 7,95
large  €10,95
=============
""")

while True:
    try:
       small = int(input("Hoeveel small pizza's wilt u: "))
       break
    except ValueError:
        print("dit is geen getal.")
while True:
    try:
        medium = int(input("Hoeveel medium pizza's wilt u: "))
        break
    except ValueError:
        print("dit is geen getal.")
while True:
    try:
        large = int(input("Hoeveel large pizza's wilt u: "))
        break
    except ValueError:
     print("dit is geen getal.")


prijs_s = small  * 5.95
prijs_m = medium * 7.95
prijs_l = large  * 10.95
totaal_prijs = float(prijs_s + prijs_m + prijs_l)

print(f"""
=======Bon=======
Pizza small : {small} €{prijs_s}
Pizza medium: {medium} €{prijs_m}
Pizza large : {large} €{prijs_l}
----------------
Prijs     : €{totaal_prijs}
=================
""")
