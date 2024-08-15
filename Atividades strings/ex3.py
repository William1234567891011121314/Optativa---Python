def getMes(numericMonth):
    if numericMonth == 1:
        mes = "janeiro"
    elif numericMonth == 2:
        mes = "fevereiro"
    elif numericMonth == 3:
        mes = "março"
    elif numericMonth == 4:
        mes = "abril"
    elif numericMonth == 5:
        mes = "maio"
    elif numericMonth == 6:
        mes = "junho"
    elif numericMonth == 7:
        mes = "julho"
    elif numericMonth == 8:
        mes = "agosto"
    elif numericMonth == 9:
        mes = "setembro"
    elif numericMonth == 10:
        mes = "outubro"
    elif numericMonth == 11:
        mes = "novembro"
    else:
        mes = "dezembro"
    return mes

data = input("Digite a data em que você nasceu (dd/mm/aaaa): ")
arrayData = data.split("/")
print(f"Você nasceu em {arrayData[0]} de {getMes(arrayData[1])} de {arrayData[2]}")