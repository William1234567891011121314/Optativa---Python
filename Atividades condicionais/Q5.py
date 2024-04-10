litros = float(input("Digite a quantidade em litros: "))
tc = input("Insira o tipo do combustível, A para álcool e G para gasolina: ")
if tc == 'A':
    if litros <= 20:
        preco = litros * (7.2*0.97)
    else:
        preco = litros * (7.2*0.95)
    print(f"O preço a ser pago é de: R${preco}")
elif tc != 'G':
    print("Combustível inválido!")
else:
    if litros <= 20:
        preco = litros * (6.5*0.96)
    else:
        preco = litros * (6.5*0.94)
    print(f"O preço a ser pago é de: R${preco}")