#jowad al fartousy
import random
kaartkleur = ("harten","klaver","schoppen","ruiten",)
kaartsoort = ("2","3","4","5","6","7","8","9","10","boer","heer","vrouw","aas")
deck= ["joker","joker"]
teller = 0

for x in range(len(kaartkleur)):
    for y in range(len(kaartsoort)):
        mix = (f"{kaartkleur[x]} {kaartsoort[y]}")
        deck.append(mix)
random.shuffle(deck)

for z in range(1,8):
    print(f'Kaart {z}: {deck[z]}')
    deck.pop(0)
print("")
print(f"""deck ({len(deck)} kaarten):
{deck}""")


