file = open('liczby1.txt')

def nwd(n1, n2):

    if n1 == n2:
        return n1
    if n1 % n2 == 0:
        return n2
    if n2 % n1 == 0:
        return n1
    for i in range(min(n1 ,n2)//2, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i

data = []
for f in file:
    data.append(f.strip())

counter = 0
for d in data:
    n1 = int(d[:len(d)//2])
    n2 = int(d[len(d)//2:])
    if nwd(n1, n2) == 1:
        counter += 1

print(counter)

SortedNumbers  = []
for d in set(data):
    SortedNumbers.append(sorted(d))

temp = []
counter2 = 0
for i in range(len(SortedNumbers)):
    for s in SortedNumbers[i+1:]:
        if SortedNumbers[i] == s:
            counter2 += 1
            temp.append([s,SortedNumbers[i]])
print(counter2, *temp)