import numpy
quantidade_notas = int(input("Quantas notas você têm?: "))
notas = numpy.zeros(quantidade_notas)
notas_sum = 0

for i in range(quantidade_notas):
    notas[i] = float(input(f"Digite a sua {i+1}º nota: "))
    notas_sum += notas[i]

media = notas_sum / quantidade_notas

if media >= 7:
    if media == 10:
        print("Aprovado com distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")

print(f"Média: {media}")