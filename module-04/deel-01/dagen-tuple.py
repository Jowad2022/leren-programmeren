dagen = ("maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag")

for x in range(len(dagen)):
    print(dagen[x])
print("")
for x in range(len(dagen)-2):
    print(dagen[x])
print("")
print(dagen[5:7])
print("")
print(dagen[::-1])
print("")
print(dagen[-3::-1])
print("")
print(dagen[-1:-3:-1])