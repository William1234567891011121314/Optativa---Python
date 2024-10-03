import numpy as numpy

m = numpy.zeros((5, 5))

for i in range(0, 5):
    for x in range(0, 5):
        m[i][x] = float(input(f"Digite um número para a posição {i+1}, {x+1}: "))

sum = 0

for x in range(0, 5):
    sum += m[x][x]

print(sum)