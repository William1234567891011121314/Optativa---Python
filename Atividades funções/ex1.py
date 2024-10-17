def maior(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

number = int(input("Digite um número: "))
number2 = int(input("Digite um segundo número: "))
print(f"O maior número é: {maior(number, number2)}")