cod = int(input("Digite o código do produto (inteiro): "))
if cod < 2:
    tipo = "Alimento não-perecível"
elif cod >= 2 and cod <= 4:
    tipo = "Alimento perecível"
elif cod >= 5 and cod <= 6:
    tipo = "Vestuário"
elif cod == 7:
    tipo = "Higiene pessoal"
elif cod >= 8 and cod <= 15:
    tipo = "Limpeza e utensílios domésticos"
else:
    tipo = "Inválido"

print(f"O tipo do produto é: {tipo}")