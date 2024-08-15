x = []
for i in range(0, 10):
    x.append(int(input(f"Digite o {i+1}º valor: ")))

for i in range(0, len(x)):
    if x[i] % 2 == 0:
        x[i] = x[i]*i
    else:
        x[i] = i
    print(x[i])