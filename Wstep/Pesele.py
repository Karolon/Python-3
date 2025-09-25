file = open('Pesele.txt')

data = []
for f in file:
    data.append(f.strip())

counterA = 0
for d in data:
    if d [4:6] == '24':
        counterA += 1

print(counterA)