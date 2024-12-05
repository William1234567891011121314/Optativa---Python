com = input("Digite o tipo de combustível:\nA - Álcool\nG - Gasolina\n\nSua resposta: ")
volume = float(input("Digite quantos litros você deseja: "))
price = 0

if com.upper() == 'A' and volume <= 20:
    price = (volume*1.9) - (1.9*0.03*volume)
elif com.upper() == 'A' and volume > 20:
    price = (volume*1.9) - (1.9*0.05*volume)

if com.upper() == 'G' and volume <= 20:
    price = (volume*2.5) - (2.5*0.04*volume)
elif com.upper() == 'G' and volume > 20:
    price = (volume*2.5) - (2.5*0.06*volume)

if com.upper() != 'G' and com.upper() != 'A':
    print("Opção inválida!")
else:
    print(f"Valor a ser pago: R${price}")