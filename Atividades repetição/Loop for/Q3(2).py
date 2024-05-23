vetor = []
for a in range(1, 11):
    n = float(input(f"Digite o {a}°: "))
    vetor.append(n)
maior = 0

for b in range(0, len(vetor)):
    if vetor[b] > maior:
        maior = vetor[b]

menor = maior

for c in range(0, len(vetor)):
    if vetor[c] < menor:
        menor = vetor[c]

print("Maior: ", maior, "\nMenor: ", menor)