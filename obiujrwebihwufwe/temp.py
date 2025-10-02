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

#c
old_d = data[1]
okresC = []
okresC_tmp = []
for i in range(1,len(data)):
    if data[i] >= data[i-1]:
        okresC_tmp.append(i)
    else:
        del okresC_tmp[:]
    if len(okresC) < len(okresC_tmp):
        okresC = []+okresC_tmp

print(okresC)