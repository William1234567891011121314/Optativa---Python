horas = float(input("Digite a quantidade de horas que você trabalha: "))
sal_hor = float(input("Digite o seu salário por hora trabalhada: "))
salario_bruto = horas*sal_hor

sindicato = salario_bruto*0.03
descontos = salario_bruto*0.03

fgts = salario_bruto*0.11
descontos = salario_bruto*0.11
ir = 0

if salario_bruto >= 1500 and salario_bruto < 2500:
    ir = salario_bruto * 0.05
    salario_liquido = salario_bruto*0.95
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.1
else:
    ir = salario_bruto * 0.2

descontos = descontos+ir

salario_liquido = salario_bruto-descontos

print(f"Salário bruto: R${salario_bruto}\nIR: R${ir}\nFGTS: R${fgts}\nTotal de descontos: R${descontos}\nSalario líquido: R${salario_liquido}")