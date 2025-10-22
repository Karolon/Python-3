file = open('ciagi.txt')

data = []
for f in file:
    f = f.strip()
    f = f.split()
    data.append(list(map(int, f)))

data = data[1::2]

counter1  = 0
maximum = 0
for d in data:
    roznica = d[1] - d[0]
    temp = True
    for i in range(1, len(d)):
        if d[i] - d[i-1] != roznica:
            temp = False
    if temp:       
        maximum = max(maximum, roznica)     
        counter1 += 1
            
print(counter1, maximum)

answer2 = []

for d in data:
    for d_ in d[::-1]:
        if (d_ ** 1/3) % 1 == 0:
            answer2.append(d_)
            break

print(answer2)


fileB = open('bledne.txt')

dataB = []
for f in fileB:
    f = f.strip()
    f = f.split()
    dataB.append(list(map(int, f)))

dataB = dataB[1::2]

answ3 = []
for d in dataB:
    dif = d[1] - d[0]

    for i in range(1, len(d)):
        if d[i] - d[i-1] != dif:
            answ3.append(d[i])
            break
            
print(answ3)