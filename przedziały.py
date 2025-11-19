data = []

x = input()
data.append(x.split(';'))
while x != '':
    x = input()
    data.append(x.split(';'))


def common_part(a, b):
    flag_a = False
    flag_b = False
    print(a,b)
    if len(a) == 2:
        flag_a = True
        a_1 = int(a[0][1:])
        a_2 = int(a[1][:-1])
    if len(b) == 2:
        flag_b = True
        b_1 = int(b[0][1:])
        b_2 = int(b[1][:-1])

    if not flag_a:
        if flag_b:
            if b_1 < int(''.join(a)) < b_2:
                return a
        else:
            return

    if not flag_b:
        if flag_a:
            if a_1 < int(''.join(b)) < a_2:
                return b
        else:
            return

    e, f = '',''

    if a_1 > b_1:
        e = a[0]
    elif a_1 == b_1:
        if a[0][1] == '<':
            e = a[0]
        else:
            e = b[0]
    else:
        e = b[0]

    if a_2 < b_2:
        f = a[1]
    elif a_2 == b_2:
        if a[1][-1] == ')':
            f = a[1]
        else:
            f = b[1]
    else:
        f = b[1]

    return f'{e};{f}'

przedzial = data[0]
for i in range(1, len(data)+1):
    c = common_part(przedzial, data[i])
    if c:
        przedzial = c
    else:
        print('posty')
        break

print(przedzial)