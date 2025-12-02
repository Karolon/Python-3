
counter = 0
def F(x):
    global counter
    counter += 1
    if x == 0:
        return 0
    else:
        return 2 + F(x//2)

print(F(511), counter)

a = F(1)
i = 2
while a < 18:
    a = F(i)
    i += 1
print(i-1)
while a <= 18:
    a = F(i)
    i += 1
print(i-1)
