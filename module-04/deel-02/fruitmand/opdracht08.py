#jowad al fartousy
from fruitmand import fruitmand

totaalgewicht = 0
watermeloen = {
    'name' : 'watermeloen',
    'weight' : 5000,
    'color' : 'green',
    'round' : True
}
fruitmand.append(watermeloen)

for x in fruitmand:
    totaalgewicht += x["weight"]
print(f"{totaalgewicht} gram")
