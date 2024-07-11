import numpy
y = 5
vetor = numpy.zeros(y)

for i in range(0, y):
    vetor[i] = int(input(f"Digite o {i}º valor: "))
sum = 0
for i in range(0, y):
    sum += vetor[i]
media = sum/y
print(f"A média é: {media}")