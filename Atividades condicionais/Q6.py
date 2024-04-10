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
print(f"{dia}/{mes}/{ano}")