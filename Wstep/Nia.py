file = open('Liczby_osemkowe.txt')

data = []
for f in file:
    data.append(f.strip())

def ifOrdered(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return 0
    return 1

counter = 0
counter2 = 0
counter3 = 0
for d in data:
    if d[0] == d[-1]:
        counter2 += 1
    d_decimal = str(int(d,8))
    if d_decimal[0] == d_decimal[-1]:
        counter3 += 1
    counter += ifOrdered(d)

print(counter, counter2, counter3)

