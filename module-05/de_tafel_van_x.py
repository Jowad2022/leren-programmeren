#jowad al fartousy

def multiplier():
    print(f"Tafel van {Tafel}:")
    for i in range(1, 11):
        print(Tafel, '*', i, '=', Tafel*i)

Tafel = int(input("Welke tafel wil je weten?: "))
multiplier()
