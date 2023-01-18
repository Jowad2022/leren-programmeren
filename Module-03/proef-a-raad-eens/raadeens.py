#jowad al fartousy
import random  
score = 0 
raden = 0
rondesInputmax = 20
#hoeveel rondes wilt de speler spelen?
def intinput(prompt):
    while True:
        try:
            I = int(input(prompt)) 
            return I
        except ValueError:
            print("Voer een getal in.")

rondesInput = intinput("Hoeveel rondes wil je spelen? : ")
while rondesInput > 20:
    print("Je kan tot 20 rondes spelen.")
    rondesInput = int(input("Hoeveel rondes wil je spelen? : ")) 
#aantal rondes per game.
while rondesInput >=1:
    print(f"je kan nog {rondesInput} rondes spelen.")
    rondesInput -= 1
    randomnmr = random.randint(1,1000)
    print(randomnmr)
    while raden <= 9:
        raden += 1
        radeninput = intinput("Wat denk je dat het getal is? : ")
        if radeninput > randomnmr:
            print ("lager")
        if radeninput < randomnmr:
            print("hoger")
        if radeninput == randomnmr:
            print("Je hebt het geraden +1 punt")
            score += 1
            opnieuw = input("Wil je weer een ronde spelen? j/n: ")
            if opnieuw == "j":
                raden = 0
            else:
                print(f"Dit is het einde van het spel je hebt {score} punten gehaald.")
        elif abs(radeninput - randomnmr) < 50:
            print()
            if abs(radeninput - randomnmr) < 20:
                print("Heel warm")
            else:
                print("warm")
        elif abs(radeninput - randomnmr) > 50:
            print()
            if abs(radeninput - randomnmr) > 20 and abs(radeninput - randomnmr) < 50:
                print("heel koud")
            else:
                print("koud")
#na 10 keer raden.
        while raden >= 10:
            print("Je bent door al je 10 kansen gegaan deze ronde.")
            opnieuw = input("Wil je weer een ronde spelen ? j/n: ")
            if opnieuw == "j":
                raden = 0
            if rondesInput < 1:
                print(f"Dit is het einde van het spel je hebt {score} punten gehaald.")