import random as rand

def zerosRemove(v):
    for x in range(0, len(v)):
        if v[x] < 0:
            v[x] = 0
    return v

v = []

for x in range(0, 15):
    v.append(int(input("Digite um número inteiro: ")))

print(zerosRemove(v))