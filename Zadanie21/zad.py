file = open('instrukcje.txt')

data = []
for f in file:
    f = f.strip().split()
    data.append(f)

counter1 = 0
instruction = ''
instructionLen = 0
letter = [0] * (ord('Z') - ord('A') + 1)
for d in data:
    if d[0] == 'DOPISZ':
        counter1 += 1
        letter[ord(d[1]) - ord('A')] += 1
    if d[0] == 'USUN':
        counter1 -= 1




tempLen = 1
for i in range(1, len(data)):
    if data[i][0] == data[i-1][0]:
        tempLen += 1
        if tempLen > instructionLen:
            instructionLen = tempLen
            instruction = data[i-1][0]
    else:
        tempLen = 1

solution = []
for d in data:
    if d[0] == 'DOPISZ':
        solution.append(d[1])
    elif d[0] == 'USUN':
        del solution[-1]
    elif d[0] == 'ZMIEN':
        del solution[-1]
        solution.append(d[1])
    else:

        i = solution.index(d[1])
        b = ord(solution[i]) + 1
        if b > ord('Z'):
            b = ord('A')
        solution[i] = chr(b)



fileAns = open('wyniki.txt', 'w')


print('1', counter1, file = fileAns)
print('2', instruction, instructionLen, file = fileAns)
print('3', chr(letter.index(max(letter)) + ord('A')), max(letter), file = fileAns)
print('4', ''.join(solution), file = fileAns)

fileAns.close()