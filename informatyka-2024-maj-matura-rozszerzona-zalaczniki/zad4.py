file = open('liczby_przyklad.txt')

data = []
for f in file:
    data.append(f.strip())

data1, data2 = data[0].split(), data[1].split()


counter1 = 0
for d1 in data1:
    d1 = int(d1)
    for d2 in data2:
        d2 = int(d2)
        if d2 % d1 == 0:
            counter1 += 1
            break

print(counter1)

#2
print(sorted(map(int, data1))[::-1][100])

#3
data1 =list(map(int, data1))
data2 = list(map(int, data2))

counter3 = []
for d2 in data2:
    temp = d2
    for d1 in data1:
        if temp % d1 == 0:
            temp //= d1
    if temp == 1:
        counter3.append(d2)

print(counter3)

#4
# biggest average, amount, start
info = [0, 0, 0]
for i in range(len(data1)):
    for j in range(i+50, len(data1)):
        avg = sum(data1[i:j+1])//len(data1[i:j+1])
        if avg > info[0]:
            info = [avg, len(data1[i:j]), i]

print(info)