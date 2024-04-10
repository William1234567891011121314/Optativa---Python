a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
if a>b and a>c:
    print(f"{a}")
    if b>c:
        print(f"{b}\n{c}")
    else:
        print(f"{c}\n{b}")
if b>a and b>c:
    print(f"{b}")
    if a>c:
        print(f"{a}\n{c}")
    else:
        print(f"{c}\n{a}")
if c>a and c>b:
    print(f"{c}")
    if a>b:
        print(f"{a}\n{b}")
    else:
        print(f"{b}\n{a}")