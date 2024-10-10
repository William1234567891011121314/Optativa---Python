negative = []
positive = []

for x in range(0, 8):
    number = int(input(f"Digite o {x+1}º número do array: "))
    if number < 0:
        negative.append(number)
    elif number > 0:
        positive.append(number)

print(f"Números negativos: {negative}, \n Números positivos: {positive}")