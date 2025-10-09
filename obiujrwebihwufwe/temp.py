file = open('TEMP.txt')

data = [int(f.strip()) for f in file]

okres = []
okres_temp = []
for i in range(len(data)):
    if (data[i]) >= 0:
        okres_temp.append(i)
    else:
        del okres_temp[:]
    if len(okres) < len(okres_temp):
        okres = []+okres_temp

print(okres, len(okres))

#b
counter = 0
avg = sum(data)/len(data)
for d in data:
    counter += 1 if d > avg else 0

print(counter)

print(sum([1 if d > sum(data)/len(data) else 0 for d in data]))

#c
okresC = []
okresC_tmp = []
for i in range(1,len(data)):
    if data[i] > data[i-1]:
        okresC_tmp.append(i-1)
    else:
        del okresC_tmp[:]
    if len(okresC) < len(okresC_tmp):
        okresC = []+okresC_tmp+[i]

print(len(okresC), okresC[0], okresC[-1], okresC)

# tmp = 0
# starting, ending, length = 0, 0, 0
# for index, d in enumerate(data[:-1]):
#     if d < data[index + 1]:
#         if tmp > length:

