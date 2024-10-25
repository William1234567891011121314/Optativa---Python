import numpy as num
import random as rand

matriz = num.zeros((4, 4))

for x in range(0, 4):
    for y in range(0, 4):
        matriz[x][y] = rand.randint(0, 20)

sum = 0
for x in range(0, 4):
    sum += matriz[x][x]

print(f"A soma dos números da diagonal principal é: {sum}")