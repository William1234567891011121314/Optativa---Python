def uniqueValues(v1, v2):
    c = []
    igual = False
    for x in range(0, vectorLength):
        igual = False
        for y in range(0, vectorLength):
            if v1[x] == v2[y]:
                igual = True
        if not igual:
            c.append(v1[x])
    return c


v1 = []
v2 = []
vectorLength = 5

for x in range(0, vectorLength):
    v1.append(int(input(f"Digite o {x+1}º elemento do primeiro vetor: ")))

for x in range(0, vectorLength):
    v2.append(int(input(f"Digite o {x+1}º elemento do segundo vetor: ")))

print(uniqueValues(v1, v2))