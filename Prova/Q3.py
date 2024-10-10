length = 100
x = []

for i in range(0, length):
    x.append(int(input(f"Digite o {i+1}º número: ")))

pares = 0
impares = 0
sum=0
for i in range(0, length):
    if x[i] %2 == 0:
        pares +=1
    else:
        impares+=1
    sum += x[i]

print(f"A média dos valores em x é: {sum/length} \nA quantidade de números pares é: {pares} \nA quantidade de números impares é: {impares}")