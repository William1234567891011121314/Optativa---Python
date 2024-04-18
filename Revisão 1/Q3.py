p1 = float(input("Digite o preço do primeiro produto: "))
p2 = float(input("Digite o preço do segundo produto: "))
p3 = float(input("Digite o valor do terceiro produto: "))

if p1<p2 :
    menor = p1
else:
    menor = p2
if menor > p3:
    menor = p3
print(f"O menor produto é o de R${menor}")