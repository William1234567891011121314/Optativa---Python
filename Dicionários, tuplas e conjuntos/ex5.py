x = []
y = []

for i in range(0, 11):
    x.append(int(input(f"Digite o {i+1}º número da lista X: ")))

for i in range(0, 11):
    y.append(int(input(f"Digite o {i+1}º número da lista Y: ")))

diferenca = []

for i in x:
    if i not in y:
        diferenca.append(i)

print(diferenca)