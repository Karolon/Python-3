file = open('liczby.txt')


data = [int(f.strip()) for f in file]


primes = []
def ifPrime(n):
    if n == 2:
        return True
    for i in range(n//2+1, 1, -1):
        if n % i == 0:
            return False
    return True
for i in range(9999):
    if ifPrime(i):
        primes.append(i)

counter1 = 0
holder1 = 0
primeDivider = []
counterSmaller = 0
counterEqual = 0
counterBigger = 0
equals = []
for d in data:
    if (d ** 0.5) % 1 == 0:
        counter1 += 1
        if not holder1:
            holder1 = d
    temp_counter = 0
    for p in primes[2:]:
        if d % p == 0:
            temp_counter += 1
    if temp_counter >= 5:
        primeDivider.append(d)

    small = int(''.join(sorted(str(d))))
    big = int(''.join(sorted(str(d), reverse=True)))
    temp = big - small
    if temp < d:
        counterSmaller += 1
    elif temp == d:
        counterEqual += 1
        equals.append(d)
    else:
        counterBigger += 1



fileAnswer = open('wyniki.txt', 'w')


print(f'1: {counter1} {holder1}', file = fileAnswer)
print(f'2: {primeDivider}', file = fileAnswer)
print(f'3:\n Mniejsza {counterSmaller}\n Równa {counterEqual} {equals}\n Więkrze {counterBigger}', file = fileAnswer)

fileAnswer.close()