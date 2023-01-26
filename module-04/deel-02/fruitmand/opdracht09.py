#jowad al fartousy
from fruitmand import fruitmand
for x in range(0, len(fruitmand)):
    if fruitmand[x].get('name') == 'druif':
        fruitmand.remove(fruitmand[x])
        break

fruitkleur = []

for x in range(len(fruitmand)):
    if fruitmand[x]["color"] not in fruitkleur:
        fruitkleur.append((fruitmand[x]["color"]))

print(fruitkleur)