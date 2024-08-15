frase = input("Digite uma frase para verificar se é palíndromo: ")
arrayFrase = list(frase)
fraseAoContrario = []

for x in range(len(frase), 0, -1):
    fraseAoContrario.append(arrayFrase[x-1])
    
fraseAoContrario = "".join(fraseAoContrario).replace(" ", "").replace(".", "")
if fraseAoContrario == frase:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo!")