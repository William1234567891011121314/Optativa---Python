palavra = input("Digite uma palavra: ")
y = []

for x in range(0, len(palavra)):
    a = True
    for i in range(0, len(y)):
        if y[i] == palavra[x]:
            a = False
            break
    print(y)
    if a:
        y.append(palavra[x])
        print(f"{palavra[x]}: {palavra.count(palavra[x])}x")
