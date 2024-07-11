vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
    vetor[i] = int(input(f"Digite o {i+1}º valor: "))

maior = 0

counter = 0
for i in range(0, 10):
    if vetor[i] > maior:
        maior = vetor[i]
        counter = i

print(f"A posição do maior número é: {counter}")

menor = maior
counter = 0
for i in range(0, 10):
    if vetor[i] < menor:
        menor = vetor[i]
        counter = i

print(f"A posição do menor número é: {counter}")