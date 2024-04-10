sex = input("Digite o seu sexo (F/M): ")
age = int(input("Digite a sua idade: "))
if age < 12:
    if sex == "M":
        print("Menina")
    else:
        print("Menino")
if age >= 12 and age <= 24:
    if sex == "M":
        print("Moça")
    else:
        print("Rapaz")
if age > 24:
    if sex == "M":
        print("Mulher")
    else:
        print("Homem")