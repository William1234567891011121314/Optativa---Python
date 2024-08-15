name = list(input("Digiet o seu nome: ").upper())
arrayName = []

for x in range(0, len(name)):
    arrayName.append(name[x])
    print("".join(arrayName))