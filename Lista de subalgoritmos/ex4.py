def sum(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1*num2

def division(num1, num2):
    if num2 == 0:
        return "Indefinido"
    return num1/num2

def calc(num1, num2, operator):
    match (operator):
        case 1:
            return sum(num1, num2)
        case 2:
            return subtraction(num1, num2)
        case 3:
            return multiplication(num1, num2)
        case 4:
            return division(num1, num2)
        case _:
            return "Operação inválida!"

operator = int(input("Digite a operação desejada:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Resultado: {calc(num1, num2, operator)}")