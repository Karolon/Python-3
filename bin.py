data = []
x = 0

start = 0
end = len(data)-1


while start < end:
    middle = (start + end) // 2 + 1
    if x == data[middle]:
        print(x)
        break
    elif x < data[middle]:
        end = middle
    else:
        start = middle

print('none in lsit')