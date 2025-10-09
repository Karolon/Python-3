file = open('dane/festyn.txt')

data_shields = []
data_n = []
data_m = []
data_t = []
temp_shields = []
temp_t = []
temp = 0
m = -1
for f in file:
    f = f.strip()
    f = f.split(' ')
    if len(f) == 1:
        if temp - m - 1 == 0:
            data_n.append(int(''.join(f)))
        if temp == 1:
            m = int(''.join(f))
            data_m.append(m)
        if temp > 1:
            temp_t.append(int(''.join(f)))
        temp += 1
        if temp_shields:
            data_shields.append(temp_shields)
            temp_shields = []
        if temp == m + 2:
            data_t.append(temp_t)
    else:
        temp_shields.append(list(map(int, f)))
        temp = 0

print( data_shields)
print(data_n)
print(data_m)
print(data_t)
print(len(data_n), len(data_m), len(data_t), len(data_shields))


for i in [0,1,2]:
    max_visible_time = 0
    counter = 0
    temp_shields = []+data_shields[i]

    for [a, b] in temp_shields:
        max_visible_time = max(max_visible_time, b)

    for t in data_t[i]:
        for j, [a, b] in enumerate(temp_shields):
            if a <= t <= a + b:
                counter += 1
                temp_shields[j] = [-1,-1]


    max_visible_second = [0, 0]
    for s in range(300):
        temp_counter = 0
        for [a, b] in data_shields[i]:
            if s >= a and s <= a + b:
                temp_counter += 1
        if temp_counter > max_visible_second[1]:
            max_visible_second = [s, temp_counter]

    temp_shields = [] + data_shields[i]
    alternative_counter = 0
    t = max(data_t[i])
    for [a, b] in temp_shields:
        if t >= a:
            alternative_counter += 1

    print(f'\nSet {i}')
    print('4.1', counter)
    print('4.2', max_visible_time)
    print('4.3', max_visible_second[1] + 1)
    print('4.3', alternative_counter)
    