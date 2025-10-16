file = open('ciagi.txt')

data = []
for f in file:
    f = f.strip()
    data.append(f)

def Prime(n):
    if n == 2:
        return True
    if n % 2 == 1:
        return False
    for i in range(3, n//2+1, 2):
        if n % i == 0:
            return False
    return True

primes = [2]
for i in range(3, max(list(map(lambda x: int(x,2), data)))//2+1, 2):
    if Prime(i):
        primes.append(i)

def HalfPrime(n):
    counter = 2
    t_n = n
    for i in primes:
        while t_n % i == 0:
            t_n //= i
            counter -= 1
            if counter < 0:
                return False

    return counter == 0


answer1 = []
counter2 = 0
counter3 = 0
holder3 = [0,0]
for d in data:
    if len(d) % 2 == 0:
        if d[:len(d)//2] == d[len(d)//2:]:
            answer1.append(d)
    flag = True
    for i in range(len(d)-1):
        if d[i] == '1' and d[i+1] == '1':
            flag = False
            break
    if flag:
        counter2 += 1

    d_ = int(d,2)
    if HalfPrime(d_):
        counter3 += 1
        if d_ > holder3[0]:
            holder3[0] = d_
        if d_ < holder3[1] or holder3[1] == 0:
            holder3[1] = d_

print(answer1)
print(counter2)
print(counter3, holder3)

