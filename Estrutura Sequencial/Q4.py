vogais = ("A", "E", "I", "O", "U")

char = input("Digite uma letra: ")

for x in range(0, len(vogais)):
    if char.upper() == vogais[x]:
        print("A letra digitada é uma vogal!")
        break