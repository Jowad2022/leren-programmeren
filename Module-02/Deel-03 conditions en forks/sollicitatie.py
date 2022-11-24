#jowad al-fartousy
print("""==================================================================================================
+                            Sollicitatieformulier "Ruimte-vuilnisman"                           +
==================================================================================================
Er word u een aantal vragen gesteld die relevant zijn voor deze positie. 
Als blijkt dat u aan de vragenlijst voeldoet dan kom u in aanmerking voor een sollicitatiegesprek. 
De vragen moeten eerlijk beantwoord worden voor een correcte resultaat!
==================================================================================================""")

naam = input("wat is uw naam?: ")
geslacht = input("wat is uw gender? man/vrouw: ")
if geslacht == "man":
    snor = input("heeft u een snor? j/n: ")
    if snor == "j":
        snor_lengte = int(input("Hoe breed is uw snor in cm? :"))
else:
    haar_kleur = input("is uw haar kleur rood? j/n: ")
    if haar_kleur == "j":
        haar_lengte = int(input("Hoelang is uw haar? :"))


diploma = input("bent u in bezit van een MBO-4 ondernemen diploma? j/n: ")
rijbewijs = input("bent u in bezit van een vrachtwagen rijbewijs? j/n: ")
hoed = input("bent u in bezit van een hoge hoed? j/n: ")
lengte = int(input("Wat is uw lengte? : "))
gewicht = int(input("Wat is uw gewicht? : "))
certificaat = input("Heeft u het overleven met gevaarlijk personeel certificaat? j/n: ")
ervaring1 = int(input("Hoeveel jaar praktijkservaring heeft u met dieren-dressuur? : "))
ervaring2 = int(input("Hoeveel jaar praktijkservaring heeft u met jongleren? : "))
ervaring3 = int(input("Hoeveel jaar  praktijkservaring heeft u met acrobatiek? : "))

if (geslacht == "man" and snor =="j" and snor_lengte <= 10 and diploma == "j" and rijbewijs == "j" and hoed == "j" and lengte >= 150 and lengte <= 220 and gewicht >= 90 and certificaat == "j" and gewicht <= 120 and ervaring1 >=4 and ervaring2 >=5 and ervaring3 >=3) or (geslacht == "vrouw" and haar_kleur == "n" and haar_lengte <=20 and diploma == "j" and rijbewijs == "j" and hoed == "j" and lengte >= 150 and lengte <= 220 and gewicht >= 90 and certificaat == "j" and gewicht <= 120 and ervaring1 >=4 and ervaring2 >=5 and ervaring3 >=3):
    print("gefeliciteerd u bent gesolliciteerd voor een vervolg gesprek.")
else:
    print("Helaas bent u niet geschikt voor deze sollicitatie.")



