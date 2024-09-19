R = []
S = []

for x in range(0, 6):
    R.append(int(input(f"Digite o {x+1}º número da lista R: ")))

for x in range(0, 11):
    S.append(int(input(f"Digite o {x+1}º número da lista S: ")))

tuple(R)
tuple(S)

X = set()

for x in R:
    X.add(x)

for x in S:
    X.add(x)

print(X)