file = open('pi.txt')

data = []
for f in file:
    data.append(int(f.strip()))

counter_list = [0]*100
counter = 0
for i in range(len(data)-1):
    n = data[i] * 10 + data[i+1]
    if data[i] == 9 and data[i+1] > 0:
        counter += 1
    counter_list[n] += 1

print(counter)

#3.2
flag = True

for c in range(len(counter_list)):
    if counter_list[c] == min(counter_list) and flag:
        print(c, counter_list[c])
        if  counter_list[c] == 0:
            flag = False
    if counter_list[c] == max(counter_list):
        print(c, counter_list[c])

#3.3

counter3 = 0
last_series = []
flag = 1
for i in range(len(data)-1):
    if data[i] < data[i+1] and flag == 1:
        last_series.append(data[i])
    if data[i] == data[i+1] and flag == 1 and len(last_series) > 2:
        last_series.append(data[i])
    else:
        last_series = []
    if 

