#jowad al fartousy
som = 50
count = 50
berekening = "50"
while som < 1000:
    count += 1
    som += count
    berekening += f" + {count}"
    print(f"{berekening} = {som}")
