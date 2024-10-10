import numpy as numpy

matriz = numpy.zeros((6, 6))

for l in range(0, 6):
    for c in range(0, 6):
       matriz[l][c] = int(input(f"Digite um número para a posição {l+1}, {c+1} da matriz: "))

print(f"Matriz digitada: \n{matriz}")

for c in range(0, 6):
    aux = matriz[1][c]
    matriz[1][c] = matriz[4][c]
    matriz[4][c] = aux

for l in range(0, 6):
    aux = matriz[l][3]
    matriz[l][3] = matriz[l][5]
    matriz[l][5] = aux

print(f"Matriz resultante: \n{matriz}")