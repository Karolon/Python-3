file = open('liczby.txt')

data = [f.strip() for f in file]

counter1 = 0
counterDiv8 = 0
counterDiv2 = 0
minimum = '100000000000000000000000000000000'
maximum = ''
for d in data:
    if d.count('0') > d.count('1'):
        counter1 += 1
    if d[-1] == '0':
        counterDiv2 += 1
    if int(d) % 1000 == 0:
        counterDiv8 += 1
    if len(d) < len(minimum):
        minimum = d
    if len(d) > len(maximum):
        maximum = d


print('1', counter1)
print('2', counterDiv2, counterDiv8)
print('3', data.index(minimum)+1, data.index(maximum)+1)