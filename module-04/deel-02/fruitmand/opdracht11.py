#jowad al fartousy
from fruitmand import fruitmand
#nieuwe lijst
kleurenlijst = []
for x in range(len(fruitmand)):
    if fruitmand[x]['color'] not in kleurenlijst:
        kleurenlijst.append((fruitmand[x]['color']))
print(f"je hebt een keuze uit deze lijst: {kleurenlijst}")
#kleur input
vraag = True
while vraag:
    vraag = input("welke kleur kies je? : ").lower()
    if vraag not in kleurenlijst:
        print("dat is niet in de lijst kies iets uit de lijst!")
    else:
        vraag = False
    

rond = 0
nietrond = 0
welrond = 0
#optelling
for x in range(len(fruitmand)):
    kleurLijst = fruitmand[x].get("color")
    if kleurLijst == vraag:
        if fruitmand[x].get("round"):
            rond += 1
            welrond += 1
        else:
            rond -= 1
            nietrond += 1
#conclusie
if welrond > nietrond:
    print(f"""
    Er zijn {rond} meer ronde vruchten dan 
    niet ronde vruchten van de kleur{vraag}
    """)
elif nietrond > welrond:
    print(f"""
    Er zijn {rond} minder ronde vruchten dan 
    ronde vruchten van de kleur '{vraag}'
    """)
else:
    print(f"""Evenveel ronde vruchten als niet ronde vruchten""")
