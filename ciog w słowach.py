word = 'MAKSYMYLIAN'

length, start, end = 0, 0, 0
tempLength = 0

for i in range(len(word)-1):
    if word[i] < word[i+1]:
        tempLength += 1
        if tempLength > length:
            length = tempLength + 1
            end = i + 1
            start = end - length + 1
    else:
        tempLength = 0

print(length, start, end)