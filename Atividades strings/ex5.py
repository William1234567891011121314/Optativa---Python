frase = input("Digite uma frase: ")
whiteSpaces = 0
vogais = 0
for x in range(0, len(frase)):
    if frase[x] == " ":
        whiteSpaces += 1
    if frase[x].upper() == "A" or frase[x].upper() == "E" or frase[x].upper() == "I" or frase[x].upper() == "O" or frase[x].upper() == "U":
        vogais +=1
print(f"A sua frase possui {whiteSpaces} espaços em branco e {vogais} vogais.")
