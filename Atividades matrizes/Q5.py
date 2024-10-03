import numpy as numpy

m = numpy.zeros((10, 10))

for i in range(0, 10):
    for x in range(0, 10):
        m[i][x] = float(input(f"Digite um número para a posição {i}, {x}: "))

sum = 0

for i in range(0, 10):
    sum += m[i][2]
print(f"O somatório dos valores da coluna 2: {sum}")

for x in range(0, 10):
    sum += m[x][x]
print(f"Somatório dos valores da diagonal principal: {sum}")