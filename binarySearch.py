import random as r

data = sorted([r.randint(-500,5000) for i in range(r.randint(123,1024))])

goal = 13
indeks  = -1

start = 0
end = len(data)
while end > start:
    middle = (end + start) // 2
    if goal == data[middle]:
        indeks = middle
        start = end
    elif goal < data[middle]:
        end = middle
    else:
        start = middle

if index_ == -1:
    print('Nie ma w liśćie')
else:
    print(indeks, data[indeks])