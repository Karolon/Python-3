file = open('PARY_LICZB.TXT')
from math import gcd
def nwd(a, b):
    for i in range(min(a, b)+1, 0, -1):
        if a % i == 0:
            if b % i == 0:
                return i

data = []
for f in file:
    data.append(list(map(int, f.strip().split())))

counter = 0
counter2 = 0
counter2_2 = 0
counter3 = 0
for d in data:
    if d[0] % d[1] == 0 or d[1] % d[0] == 0:
        counter += 1
    if nwd(d[0],d[1]) == 1:
        counter2 +=1
    counter2_2 = counter2_2 + 1 if gcd(d[0],d[1]) == 1 else counter2_2
    # if sum(list(map(int,str(d[0]).split()))) == sum(list(map(int,str(d[1]).split()))):
    #     counter3 += 1
    counter3 += 1 if sum([int(a) for a in str(d[0])]) == sum([int(b) for b in str(d[1])]) else 0
print(counter)
print(counter2)
print(counter2_2)
print(counter3)

print(sum(list(map(lambda d: 1 if sum([int(a) for a in str(d[0])]) == sum([int(b) for b in str(d[1])]) else 0, [d for d in data]))))