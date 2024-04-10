a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))
e = int(input("Digite o valor de E: "))

if a>b and a>c and a>d and a>e:
    print(f"O maior número é A ({a})")
if b>a and b>c and b>d and b>e:
    print(f"O maior número é B {b}")
if c>a and c>b and c>d and c>e:
    print(f"O maior número é C {c}")