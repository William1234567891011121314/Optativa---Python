import numpy as numpy

vetor = []
matriz = numpy.zeros((3, 3))

for l in range(0, 3):
    vetor.append(int(input(f"Digite o {l+1}º número do vetor: ")))

for c in range(0, 3):
    for l in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para a posição {l+1}, {c+1} da matriz: "))

matrizResultado = numpy.zeros((3, 3))

for l in range(0, 3):
    for c in range(0, 3):
        matrizResultado[c][l] = matriz[c][l] * vetor[c]

print(f"Matriz resultado: \n{matrizResultado}")