land1 = input("land 1 ?: ")
land2 = input("land 2 ?: ")
land3 = input("land 3 ?: ")

score_land1 = 0
score_land2 = 0
score_land3 = 0



Voor_land1 = 0
Voor_land2 = 0
Voor_land3 = 0

tegen_land1 = 0
tegen_land2 = 0
tegen_land3 = 0

print(f"""
    land 1: {land1}
    land 2: {land2}
    land 3: {land3}""")
print("Wedstrijd 1")
doelpunten_land1 = int(input(f"Doelpunten {land1}: "))
doelpunten_land2 = int(input(f"Doelpunten {land2}: "))

Voor_land1 += doelpunten_land1
tegen_land1 += doelpunten_land2
Voor_land2 += doelpunten_land2 
Voor_land2 += doelpunten_land1

if doelpunten_land1 > doelpunten_land2:
    score_land1 += 3
else:
    score_land2 += 3
    
print("Wedstrijd 2")
doelpunten_land1 = int(input(f"Doelpunten {land1}: "))
doelpunten_land3 = int(input(f"Doelpunten {land3}: "))

Voor_land1 += doelpunten_land1
tegen_land1 += doelpunten_land3
Voor_land3 += doelpunten_land3
Voor_land3 += doelpunten_land1

if doelpunten_land1 > doelpunten_land3:
    score_land1 += 3
else:
    score_land3 += 3

print("Wedstrijd 3")
doelpunten_land2 = int(input(f"Doelpunten {land2}: "))
doelpunten_land3 = int(input(f"Doelpunten {land3}: "))

Voor_land2 += doelpunten_land2
tegen_land2 += doelpunten_land3
Voor_land3 += doelpunten_land3 
Voor_land3 += doelpunten_land2

if doelpunten_land2 > doelpunten_land3:
    score_land2 += 3
else:
    score_land3 += 3
    
print(f"""
    +++++++++++++++++++++++++++++++++++
    {land1} : {score_land1} doelpunt voor: {Voor_land1} tegen: {tegen_land1}
    {land2} : {score_land2} doelpunt voor: {Voor_land2} tegen: {tegen_land2}
    {land3} : {score_land3} doelpunt voor: {Voor_land3} tegen: {tegen_land3}
    +++++++++++++++++++++++++++++++++++
    """)