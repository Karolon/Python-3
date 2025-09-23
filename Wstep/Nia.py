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
for d in data:
    if d[0] == d[-1]:
        counter2 += 1
    
    counter += ifOrdered(d)

print(counter)

