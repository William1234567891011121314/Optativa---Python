length = 25
numbers = []

for x in range(0, length):
    numbers.append(int(input(f"Digite o {x+1}º número da lista: ")))

print(numbers)
inverse = []

aux = length-1
for i in range(0, length):
    inverse.append(numbers[aux] * -1)
    aux-=1

print(f"Lista invertida: {inverse}")