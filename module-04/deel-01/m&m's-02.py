from random import randint

mm = ["rood","blauw","groen","geel","bruin"]
vraag = int(input("hoeveel m&m's moeten er toegevoegd worden aan de zak? : "))
zak = {}

for x in range(vraag):
    kleurmix = randint(0,4)
    randomKleur = mm[kleurmix]
    if mm[kleurmix] not in zak:
        zak.update({randomKleur : 1})
    else:
        x = zak.get(mm[kleurmix]) +1
        zak.update({mm[kleurmix]:x})    
print(zak)

