#jowad al fartousy
fibonacciLijst = [0, 1]
def fibonacci(x, y, z):
    if z == 2:
        return 1
    else:
        nieuwe = x + y
        x = y
        y = nieuwe
        fibonacciLijst.append(nieuwe)
        return z * fibonacci(x, nieuwe, z-1)

vraag = int(input("Hoeveel?"))
fibonacci(0, 1, vraag)
print(fibonacciLijst)