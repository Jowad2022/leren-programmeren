#Jowad al-fartousy,pizzaCalculator

print("""=====Menu====
Small  € 5.95
meduim € 7,95
large  €10,95
=============
""")

small = int(input("Hoeveel small pizza's wilt u: "))
medium = int(input("Hoeveel medium pizza's wilt u: "))
large = int(input("Hoeveel large pizza's wilt u: "))
prijs_s = small  * 5.95
prijs_m = medium * 7.95
prijs_l = large  * 10.95
totaal_prijs = float(prijs_s + prijs_m + prijs_l)

print(f"""
=======Bon=======
Pizza small : {small}
Pizza medium: {medium}
Pizza large : {large}
----------------
Prijs     : €{totaal_prijs}
=================
""")