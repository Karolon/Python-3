from binarySearch import BinarySearch

fileFree = open('miejsca.txt')
fileReserved = open('rezerwacje.txt')

data = []
for f in fileFree:
    f = f.strip()
    data.append(int(f))



reserved = []
for f in fileReserved:
    f = f.strip()
    reserved.append(int(f))

for r in reserved:
    b = BinarySearch(data, r)
    if b is not None:
        print(b)
    else:
        print('Nie ma takiego miejsca w samolocie')
