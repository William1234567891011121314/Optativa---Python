data = input("Digite uma data no formato dd/mm/aaaa: ")
data = data.split('/')
print(data)

for i in range(0, len(data)):
    data[i] = int(data[i])

correct_month = False
correct_day = False
correct_year = False

if data[1] % 2 == 0 and data[1] <= 7:
    if data[1] == 2:
        if data[2] % 400 == 0 or (data[2] % 100 == 0 and data[2] % 400 != 0):
            if data[0] == 29:
                correct_day = True
        else:
            if data[0] == 28:
                correct_day = True
    else:
        if data[0] == 30:
            correct_day = True
else:
    if data[0] == 31:
        correct_day = True

if data[2] >= 0:
    correct_year = True
if data[1] >=1 and data[1] <=12:
    correct_month = True

if correct_month and correct_day and correct_year:
    print("Data válida!")
else:
    print("Data inválida!")