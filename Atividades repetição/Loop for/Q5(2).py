counter = 0
for c in range(0, 15):
    x = float(input(f"Digite o {c+1}° número: "))
    if x>30:
        counter+=1
if counter == 1:
    print("Você digitou 1 número maior que 30")
else:
    print(f"Você digitou {counter} números maiores que 30")