def NieparzystySkrot(n):
    m = 0
    b = 1
    while n > 0:
        a = n % 10
        n //= 10
        if a % 2 != 0:
            m+= b * a
            b *= 10
    if m == 0:
        return 0
    return m

print(NieparzystySkrot(39101))

file = open('skrot.txt')

data = []
for f in file:
    f = f.strip()
    data.append(int(f))

maximum = 0
counter2 = 0
for d in data:
    if not NieparzystySkrot(d):
        counter2 += 1
        maximum = max(maximum, d)

print(counter2)
print(maximum)