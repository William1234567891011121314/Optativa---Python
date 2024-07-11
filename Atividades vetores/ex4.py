import numpy
y = 5
vetor = numpy.zeros(y)

for i in range(0, y):
    vetor[i] = int(input(f"Digite o {i}º valor: "))
maior = 0
for i in range(0, y):
    if vetor[i] > maior:
        maior = i
menor = maior
for i in range(0, y):
    if vetor[i] < menor:
        menor = i
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")