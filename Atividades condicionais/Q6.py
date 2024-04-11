dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Dgite o ano:"))
sdias = int(input("Digite a quantidade de dias a ser somada: "))
diastt = ano*365 + mes*30 + dia
diastt += sdias
mes = diastt%365
ano = diastt/365 - mes/365
dia = mes%30
mes = mes/30 - mes%30/30
if dia == 0:
    dia = 30
    mes -= 1
print(f"{dia:.0f}/{mes:.0f}/{ano:.0f}")