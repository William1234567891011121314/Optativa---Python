x = []
for i in range(0, 5):
    x.append(int(input(f"Digite o {i+1}º valor: ")))

y = []
for i in range(0, 5):
    y.append(int(input(f"Digite o {i+1}º valor: ")))

z = []
for i in range(0, len(y)):
    z.append(x[i]+y[i])

print(z)