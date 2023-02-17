#jowad al fartousy
fibonacciLijst = [0,1]

def fibonacci(input):
    x, y = 0, 1
    for z in range(input):
        nieuwe = x + y
        x = y
        y = nieuwe
        fibonacciLijst.append(nieuwe)
    return

vraag = int(input("Hoeveel getallen?"))
fibonacci(vraag)
print(fibonacciLijst)
lengte = len(fibonacciLijst)

print(f"""
==============================================
De laatste 2 van de reeks gedeeld door elkaar: 
{fibonacciLijst[lengte - 1] / fibonacciLijst[lengte - 2]}
==============================================
""")