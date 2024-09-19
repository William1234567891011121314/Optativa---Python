lista = []

for x in range(0, 10):
    lista.append(int(input(f"Digite o {x}º número da lista: ")))

for x in range(0, 10):
    contador = 0
    pos = x
    for y in range(1, lista[x]+1):
        if lista[x] % y == 0:
            contador += 1
    if contador == 2:
        print(f"O número {lista[x]} localizado na {x}º posição é primo")