sum = 0
ncounter = 0
for c in range(0, 20):
    x = float(input(f"Digite o {c+1}° número: "))
    if x<0:
        ncounter+=1
    else:
        sum+=x
if ncounter == 1:
    print("Você digitou 1 número negativo")
else:
    print(f"Você digitou {ncounter} números negativos")
print(f"A soma total dos positivos é: {sum}")