countern = 0
for i in range(1, 200):
    if countern > 10:
        break
    counter = 0
    for c in range(1, i+1):
        if i%c == 0:
            counter += 1
    if counter == 2:
        countern += 1 
        print(i)