nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2
print(media)

if media >= 9:
    print("Nota: A")
elif media < 9 and media >= 7.5:
    print("Nota: B")
elif media < 7.5 and media >=6:
    print("Nota: C")
elif media < 6 and media >=4:
    print("Nota: D")
else:
    print("Nota: E")

if media >= 6:
    print("APROVADO")
else:
    print("REPROVADO")