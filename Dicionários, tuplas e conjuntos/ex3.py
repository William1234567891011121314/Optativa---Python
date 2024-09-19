k = []

for x in range(0, 21):
    k.append(int(input(f"Digite o {x+1}º número do conjunto K: ")))

for x in range(1, len(k), 2):
    aux = k[x-1]
    k[x-1] = k[x]
    k[x] = aux

print(k)