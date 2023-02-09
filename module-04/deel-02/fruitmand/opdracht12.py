from fruitmand import fruitmand
namenlijst = []
lengte = 0
for x in range(0, len(fruitmand)):
    namenlijst = len(fruitmand[x].get("name"))
    if namenlijst > lengte:
        lengte = namenlijst

for x in range(0, len(fruitmand)):
    if  lengte == len(fruitmand[x].get("name")):
        naam = fruitmand[x].get("name")
        kleur = fruitmand[x].get("color")
        gewicht = fruitmand[x].get("weight")


def vertaling_van_kleuren(fruit:str):
    lijst ={
        "green" : "groene",
        "red" : "rode",
        "orange" : "oranje",
        "brown" : "bruin",
        "black" : "zwart",
        "yellow" : "gele",
        "blue" : "blauw",
        "purple" : "paars",
        "pink" : "roze"
    }
    return lijst[fruit]

print(f'De "{naam}" ({lengte} letters) heeft een {vertaling_van_kleuren(kleur)} kleur en een gewicht van  {gewicht / 1000} kg.')