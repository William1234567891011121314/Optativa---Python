import numpy
numbers = numpy.zeros(3)

for x in range(0, 3):
    numbers[x] = float(input(f"Digite o preço do {x+1}º produto: "))

menor = numbers[0]
for x in range(0, len(numbers)-1):
    if numbers[x] < numbers[x+1]:
        menor = numbers[x]
    else:
        menor = numbers[x+1]

print(f"O produto de menor preço é {menor}")