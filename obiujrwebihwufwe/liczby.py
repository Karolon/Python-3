file = open('LICZBY.txt')

data = [f.strip() for f in file]

#a
counter  = 0
for d in data:
    flag = 1
    for l in d:
        if l not in '24680':
            flag = 0
    counter += flag

print(counter)

#b
counter1 = 0
for d in data:
    if d == d[::-1]:
        counter1 += 1

print(counter1)

#c
suma = []
maximum = 0
for d in data:
    tmp = d
    suma_tmp = sum(list(map(int, list(d))))
    suma.append(suma_tmp)
    if maximum < suma_tmp:
        maximum = suma_tmp
        maximum_number = tmp

print(suma)
print(maximum, maximum_number)


