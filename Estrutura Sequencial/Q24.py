def verifier(res):
    if res % 2 == 0:
        print("Esse número par")
    else:
        print("Esse núemro é ímpar")

    if res > 0:
        print("Esse número é positivo")
    elif res < 0:
        print("Esse número é negativo")
    else:
        print("Esse número é nulo")
    
    if res // 1 == res:
        print("Esse número é inteiro")
    else:
        print("Esse número é decimal")

n1 = float(input('Informe n1: '))
n2 = float(input('Informe n2: '))
op = input('Informe a operacao(+-*/): ')

if op == '+':
    print(f"{n1} {op} {n2} = {n1 + n2}")
    verifier(n1+n2)
elif op == '-':
    print(f"{n1} {op} {n2} = {n1 - n2}")
    verifier(n1-n2)
elif op == '*':
    print(f"{n1} {op} {n2} = {n1 * n2}")
    verifier(n1*n2)
elif op == '/':
    print(f"{n1} {op} {n2} = {n1 / n2}")
    verifier(n1/n2)
else:
    print("Operação inválida!")