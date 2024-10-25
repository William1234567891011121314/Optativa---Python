import numpy as num
import random as rand

matriz = num.zeros((5, 5))

for x in range(0, 5):
    for y in range(0, 5):
        matriz[x][y] = rand.randint(0, 100)

sum = 0
for x in range(0, 5):
    for y in range(0, 5):
        sum += matriz[x][y]

print(f"A soma de todos os elementos é: {sum}")