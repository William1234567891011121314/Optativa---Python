x = float(input("Digite o valor para X: "))
y = float(input("Digite o valor para Y: "))
if (x+y)*0.3 >= 500:
    aux = x
    x = y
    y = aux
    print(f"O valor de Y é {y} e o valor de X é {x}.")
else:
    if x>y:
        print("X é maior que Y.")
    else:
        print("Y é maior que X.")