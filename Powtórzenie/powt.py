
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_half_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0 and is_prime(i) and is_prime(n//i):
            return True
    return False

file = open("liczby (3).txt")

data = [int(f.strip()) for f in file]

min_half_prime = 1000000000000000000000000000000000000000000000000000000
max_half_prime = 0
length, min_chain = 0, 0
tmp_len = 1
for d in data:
    if is_half_prime(d):
        min_half_prime = min(min_half_prime, d)
        max_half_prime = max(max_half_prime, d)

for i in range(1,len(data)):
    if data[i] < data[i-1]:
        if is_prime(data[i]) and is_prime(data[i-1]):
            tmp_len += 1
            if tmp_len > length:
                length = tmp_len
                min_chain = data[i]
    else:
        tmp_len = 1




file2 = open("answer.txt", 'w')
print(max_half_prime - min_half_prime, file = file2)
print(length, min_chain, file = file2)
file2.close()