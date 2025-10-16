from math import gcd
from pkgutil import get_data

file = open('dane_ulamki.txt')

data = []

for f in file:
    f = f.strip()
    f = f.split()
    data.append(list(map(int, f)))

counter2 = 0
counter3 = 0
minimal = data[0]
sum4 = 0
constant_b = 2*2*3*3*5*5*7*7*13
for d in data:
    a, b = d
    if minimal[0]/minimal[1] >= a/b:
        if minimal[0]/minimal[1] == a/b:
             if b < minimal[1]:
                minimal = d
        else:
            minimal = d

    if gcd(a, b) == 1:
        counter2 += 1

    counter3 += a//gcd(a, b)

    sum4 += a*constant_b//b

file_ans = open('wyniki_ulamki.txt', 'w')
print('4.1',*minimal, file=file_ans)
print('4.2',counter2, file=file_ans)
print('4.3',counter3, file=file_ans)
print('4.4',sum4, file=file_ans)