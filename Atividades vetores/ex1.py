import numpy
y = 10
x = numpy.zeros(y)

for i in range(0, y):
    z = float(input(f"Digite o {i+1}º valor: "))
    x[i] = z
for i in range(0, y):
    print(f"{i+1}º valor: {x[i]}")