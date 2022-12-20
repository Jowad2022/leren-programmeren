#jowad al fartousy
count = 0
x = 1
y = 100
while x != y:
    count +=1
    vraag = input("? : ")
    if vraag == "quit":
        break
if vraag =="quit":
    print(f"zo vaak is ? gevraagd: {count}.")

