name = input("Digite o seu nome: ")

upperName = list(name.upper())
newName = []

for x in range(len(upperName), 0, -1):
    newName.append(upperName[x-1])
    print(x)
print("".join(newName))