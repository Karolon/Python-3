counter = 0
b = 1
c = 0
n = 333333666666999999
while n > 0:
    a = n % 10
    n //=  10
    if a % 2 == 0:
        c += b * (a // 2)
    else:
        c += b
        counter += 1
    b *= 10

print(c, counter)