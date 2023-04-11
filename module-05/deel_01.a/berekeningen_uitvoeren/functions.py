def plus(n1 : float, n2 : float):
    answer = n1 + n2
    return answer

def min(n1 : float, n2 : float):
    answer = n1 - n2
    return answer

def keer(n1 : float, n2 : float):
    answer = n1 * n2
    return answer

def delen(n1 : float, n2 : float):
    answer = n1 / n2
    return answer

def numberInput():  
    while True:
        try:
            number = float( input("Voer een nummer in: "))
            break
        except:
            print("Voer een geldig nummer in.")
    return number
