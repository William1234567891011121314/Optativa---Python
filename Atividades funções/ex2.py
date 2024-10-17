def par(num):
    if num % 2 == 0:
        return True
    return False

number = int(input("Digite um número: "))
if par(number):
    print("O número é par!")
else:
    print("O número é impar!")