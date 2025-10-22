file = open('instrukcje.txt')

data = []
for f in file:
    f = f.strip().split()
    data.append(f)

counter1 = 0
instruction = ''
instructionLen = 0
for d in data:
    if d[0] == 'DOPISZ':
        counter1 += 1
    if d[0] == 'USUN':
        counter1 -= 1

for i in range(1, len(data)):
    tempLen = 0
    if data[i][0] == data[i-1][0]:
        tempLen += 1
    elif tempLen > 

print(counter1)