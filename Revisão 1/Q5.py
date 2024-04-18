cargo = int(input("Digite o seu código: "))
salario = float(input("Digite o seu salário atual: "))
if cargo == 1:
    salario*=1.5
    aumento = "50%"
elif cargo == 2:
    salario*=1.35
    aumento = "35%"
elif cargo == 3:
    salario*=1.2
    aumento = "20%"
elif cargo == 4:
    salario*=1.1
    aumento = "10%"
elif cargo == 5:
    aumento = "0%"
else:
    print("Código inválido!")
print(f"O seu salário é de {salario}, e você teve um aumento de {aumento}")