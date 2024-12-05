def calc(a):
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b*b) -4*a*c
    if delta < 0:
        print("Essa equação não possui raízes reais!")
    elif delta == 0:
        raiz = (-1*b)/2*a
        print(f"Essa equação possui apenas uma raíz!\nRaíz: {raiz}")
    else:
        raiz_pos = (-1*b) + (delta)^0.5/2*a
        raiz_neg = (-1*b) - (delta)^0.5/2*a
        print(f"Raíz positiva: {raiz_pos}\nRaíz negativa: {raiz_neg}")

a = float(input("Digite o valor de a: "))
if a == 0:
    print("Isso não é uma equação de segundo grau!")
else:
    calc(a)