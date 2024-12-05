turno = input("Digite o turno em que você estuda:\nM - Matutino\nV - Vespertino\nN - Noturno\n\nValor informado: ")

if turno.upper() == 'M':
    print("Bom dia!")
elif turno.upper() == 'V':
    print("Boa tarde!")
elif turno.upper() == 'N':
    print("Boa noite!")
else:
    print("Valor inválido!")