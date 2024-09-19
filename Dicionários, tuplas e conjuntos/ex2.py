import random

gabarito = set()

for x in range(0, 5):
    gabarito.add(random.randint(1, 100))

aux = 0
aposta = []

while(aux <= 10):
    numeroAposta = int(input(f"Digite o {aux+1}º número de aposta: "))
    if(numeroAposta in aposta):
        print("Você não pode digitar um número repetido!")
    else:
        aposta.append(numeroAposta)
        aux+=1

tuple(aposta)

pontos = 0

for x in aposta:
    if(x in gabarito):
        pontos +=1

print(f"Você fez {pontos} pontos.")
print(f"Gabarito: {gabarito}")

if pontos == 5:
    print("Parabéns! Você ganhou o prêmio máximo!")