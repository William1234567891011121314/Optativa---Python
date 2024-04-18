n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = ((n1*3)+(n2*2)+(n3*5))/(3+2+5)
print(f"A média ponderada é: {media}")

if media >= 6:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado :(")