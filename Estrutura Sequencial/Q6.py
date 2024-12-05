import numpy
numbers = numpy.zeros(3)

for x in range(0, 3):
    numbers[x] = float(input(f"Digite o {x+1}º número: "))

maior = numbers[0]
for x in range(0, len(numbers)-1):
    if numbers[x] > numbers[x+1]:
        maior = numbers[x]
    else:
        maior = numbers[x+1]

print(f"O maior número é {maior}")