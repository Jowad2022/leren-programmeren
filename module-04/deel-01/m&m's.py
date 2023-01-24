#jowad al fartousy
import random
mm = ("oranje","blauw","groen","bruin")
legezak = []
vraag1 = int(input("hoeveel m&m's moeten er in de zak?: "))
for x  in range(vraag1):
    kleur = random.choice(mm)
    legezak.append(kleur)
print(legezak)
