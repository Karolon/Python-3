from sys import flags

file1 = open('dane_systemy1.txt')
file2 = open('dane_systemy2.txt')
file3 = open('dane_systemy3.txt')

data1 = [f.strip().split() for f in file1]
data2 = [f.strip().split() for f in file2]
data3 = [f.strip().split() for f in file3]


smallest1, smallest2, smallest3  = 1000, 1000, 1000


for d in data1:
    d_ = int(d[1], 2)
    if d_ < smallest1:
        smallest1 = d_

for d in data2:
    d_ = int(d[1], 4)
    if d_ < smallest2:
        smallest2 = d_

for d in data3:
    d_ = int(d[1], 8)
    if d_ < smallest3:
        smallest3 = d_

print(bin(smallest1).replace('0b',''), bin(smallest2).replace('0b',''), bin(smallest3).replace('0b',''))

#6.2
record1, record2, record3 = int(data1[0][1],2), int(data2[0][1],4), int(data3[0][1],8)
record_counter = 1
counter2 = 0
for i in range(len(data1)):
    if (int(data1[i][0], 2) - 12) % 24 != 0 and (int(data2[i][0], 4) - 12) % 24 != 0 and (int(data3[i][0], 8) - 12) % 24 != 0:
        counter2 += 1

    flag = True
    if int(data1[i][1], 2) > record1:
        record1 = int(data1[i][1], 2)
        record_counter += 1
        flag = False
    if int(data2[i][1], 4) > record2:
        record2 = int(data2[i][1], 4)
        if flag:
            record_counter += 1
            flag = False
    if int(data3[i][1], 8) > record3:
        record3 = int(data3[i][1], 8)
        if flag:
            record_counter += 1
            flag = False


print(counter2)
print(record_counter)

#6.3

