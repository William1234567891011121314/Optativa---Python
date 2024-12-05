opc_carne = int(input("Digite o tipo de carne desejado:\n1 - Filé Duplo\n2 - Alcatra\n3 - Picanha\n\nSua resposta: "))
quantidade = float(input("Digtite a quantidade desejada (Kg): "))
preco = 0
aux = True
while True:
    match(opc_carne):
        case 1:
            if quantidade <= 5:
                preco = quantidade*4.9
            else:
                preco = quantidade*5.8
            break
        case 2:
            if quantidade <= 5:
                preco = quantidade*5.9
            else:
                preco = quantidade*6.8
            break
        case 3:
            if quantidade <= 5:
                preco = quantidade*6.9
            else:
                preco = quantidade*7.8
            break
        case _:
            print("Opção inválida!")
            aux = False
            break
    if aux:
        break
desconto = 0
opc = int(input("Você deseja utilizar qual método de pagamento?\n1 - Pix\n2 - Cartão de débito\n3 - Cartão de crédito\n4 - Cartão Tabajara (receba 5% de desconto!)\n\nSua resposta: "))
if opc == 4:
    preco *= 0.95
    desconto = 5

pagamentos = ('Pix', 'Cartão de débito', 'Cartão de crédito', 'Cartão Tabajara')
carnes = ('Filé Duplo', 'Alcatra', 'Picanha')

print(f"Tipo de carne: {carnes[opc_carne - 1]}\nQuantidade: {quantidade} Kg\nPreço: R${preco+desconto}\nTipo de pagamento: {pagamentos[opc - 1]}\nDesconto: {desconto}%\nPreço a pagar: R${preco}")