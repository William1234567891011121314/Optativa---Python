def triangleArea(base, heigth):
    return heigth*base/2

base = int(input("Digite o tamanho da base do seu triângulo: "))
heigth = int(input("Digite a altura do seu triângulo: "))
print(f"A área do seu quadrado é: {triangleArea(base, heigth)}")