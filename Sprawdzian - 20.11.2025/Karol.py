
file = open('liczby.txt')

data  = []
for f in file:
    f = f.strip().split()
    data.append(f)

file_ans = open('Karol.txt', 'w')

#1
line = 0
letter_dif = 0
for i, d in enumerate(data):
    tmp_set = set()
    for l in d[0]:
        tmp_set.add(l)
    tmp_dif = len(tmp_set)
    if tmp_dif >= letter_dif:
        line = i + 1
        letter_dif = tmp_dif

print('Zad 1', line, file=file_ans)
#2
def amstrong(n):
    suma = 0
    for i in n:
        suma += int(i)**len(n)
    return suma == int(n)

ciog_start, ciog_end, ciog_len = -1, -1, 0
tmp_start, tmp_end, tmp_len = -1, -1, 0
for i in range(len(data)):
    a = data[i][1]
    if amstrong(a):
        if tmp_len == 0:
            tmp_start = a
        tmp_end = a
        tmp_len += 1
        if ciog_len < tmp_len:
            ciog_len = tmp_len
            ciog_end = tmp_end
            ciog_start = tmp_start
    else:
        tmp_start, tmp_end, tmp_len = -1, -1, 0

print(f'Zad 2\nDługość{ciog_len}\nStart{ciog_start}\nKoniec{ciog_end}', file=file_ans)

#3
answer = []

for d in data:
    if 0 < len(d[0]) <= 100:
        answer.append([len(d[0]), d[0]])

print('Zad 3',*answer, sep='\n', file=file_ans)

#4
def silnia(n):
    if n == 1:
        return 1
    return silnia(n-1) * n

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n//2, 2):
        if n % i == 0:
            return False
    return True

prime_list = []
for d in data:
    if prime(int(d[1])):
        prime_list.append(int(d[1]))

prime_list.sort()
print('Zad 4\n piąty najmniejszy prime', prime_list[4], file=file_ans)
#answer4 = silnia(prime_list[4])
#print(answer4)

#5
def binary_search(list, szukana):
    left = 0
    right = len(list) - 1
    while left < right:
        midd = (left + right)//2
        if list[midd] == szukana:
            return midd
        elif list[midd] < szukana:
            left = midd
        elif list[midd] > szukana:
            right = midd

    return 'nie ma'

