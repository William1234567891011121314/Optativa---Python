x = int(input("Digite o número do intervalo inferior: "))
y = int(input("Digite o número do intervalo superior: "))
z = 0
for c in range(x+1, y):
    if c%2 == 0:
        z+=c
print(f"{z}")