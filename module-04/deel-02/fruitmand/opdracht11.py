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
    vraag1 = input("welke kleur kies je? : ").lower()
    if vraag1 not in kleurenlijst:
        print("dat is niet in de lijst kies iets uit de lijst!")
    else:
        vraag = False
rond = 0
nietrond = 0
welrond = 0
#optelling
for x in range(len(fruitmand)):
    kleurLijst = fruitmand[x].get("color")
    if kleurLijst == vraag1:
        true_false = fruitmand[x].get("round")
        if true_false == True:
            welrond += 1
            rond += 1
        else:
            nietrond += 1
            rond -= 1
#conclusie
if welrond > nietrond:
    print(f"""
    Er zijn {welrond} meer ronde vruchten dan 
    niet ronde vruchten van de kleur{vraag1}
    """)
elif nietrond > welrond:
    print(f"""
    Er zijn {nietrond} minder ronde vruchten dan 
    ronde vruchten van de kleur '{vraag1}'
    """)
else:
    print(f"Evenveel ronde vruchten als niet ronde vruchten")
