#jowad al fartousy
from fruitmand import fruitmand
import random

vraag = int(input("hoeveel fruiten wil je zien ? :"))
for x in range(vraag):
    randomfruit = random.choice(fruitmand)
    print(randomfruit['name'])