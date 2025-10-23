file = open('punkty.txt')

data = []
for f in file:
    f = f.strip().split()
    data.append(f)


def IsPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(3, n//2+1, 1):
        if n % i == 0:
            return False
    return True


counter1 = 0
counter2 = 0
farthestPoints = [[0,0],[0,0]]
farthestPointsDistant = 0
counterInside, counterOn, counterOutside = 0,0,0
for d in data:
    x = int(d[0])
    y = int(d[1])
    if IsPrime(x) and IsPrime(y):
        counter1 += 1

    if set(d[1]) == set(d[0]):
        counter2 += 1

    for d_ in data:
        x_ = int(d_[0])
        y_ = int(d_[1])

        if farthestPointsDistant < ((x_ - x)**2 + (y_ - y)**2)**1/2:
            farthestPoints = [[x,y],[x_, y_]]
            farthestPointsDistant = ((x_ - x)**2 + (y_ - y)**2)**1/2

    if abs(x) > 5000 or abs(y) > 5000:
        counterOutside += 1
    elif (abs(x) < 5000 and abs(y) != 5000) or (abs(y) < 5000 and abs(x) != 5000):
        counterInside += 1
    else:
        counterOn += 1


fileAns = open('wyniki.txt', 'w')

print('1', counter1, file = fileAns)
print('2', counter2, file = fileAns)
print('3', farthestPoints, farthestPointsDistant, file = fileAns)
print(f'4 w środku {counterInside}\nna {counterOn}\npoza {counterOutside}', file = fileAns)

