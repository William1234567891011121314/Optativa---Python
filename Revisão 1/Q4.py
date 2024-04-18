ano = int(input("Digite o ano atual: "))
anodenascimento = int(input("Digite o ano de nascimento: "))

if ano - anodenascimento < 16:
    print("Infelizmente você não pode votar.")
else:
    print("Você pode votar!")