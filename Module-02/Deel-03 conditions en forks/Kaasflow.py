#Jowad al-fartousy
start = input("is de kaas geel? j/n: ")
if start == "j":
    gaten = input("zitten er gaten in? j/n: ")
    if gaten == "j":
        duur = input("is de kaas belagelijk duur? j/n: ")
        if duur == "j":
             print("Emmenthaler")
        else:
             print("leerdammer")
    else :
        steen = input("is de kaas hard als steen? j/n: ")
        if steen == "j":
            print("parmigiano")
        else:
            print("goudse kaas")
else: 
    blauw = input("heeft de kaas blauwe schimmel? j/n: ")
    if blauw == "j":
        korst = input("heeft de kaas een korst? j/n: ")
        if korst == "j":
            print("blue de rochbaron")
        else: 
            print("foume dámbert")
    else: 
        korst2 = input("heeft de kaas een korst? j/n: ")
        if korst2 == "j":
             print("camembert")
        else: 
             print("mozzarella")
        
