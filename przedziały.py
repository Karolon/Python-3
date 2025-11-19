from math import trunc

data = []


check = True
while check:
    x = input()
    if x != '':
       data.append(x.split(';'))
    else:
        check = False


def common_part(a, b):
    flag_a = False
    flag_b = False
    if len(a) == 2:
        flag_a = True
        a_1 = float(a[0][1:])
        a_2 = float(a[1][:-1])
    if len(b) == 2:
        flag_b = True
        b_1 = float(b[0][1:])
        b_2 = float(b[1][:-1])

    e, f = '', ''
    if (not flag_a) and (not flag_b):
        if a == b:
            return a
        else:
            return

    elif not flag_a:
        a_ = float(''.join(a))
        if b_1 < a_ < b_2:
            return a
        elif (b_1 == a_ and b[0][0] == '<') or (b_2 == a_ and b[1][-1] == '>'):
            return a
        else:
            return


    elif not flag_b:
        b_ = float(''.join(b))
        if a_1 < b_ < a_2:
            return b
        elif (a_1 == b_ and a[0][0] == '<') or (a_2 == b_ and a[1][-1] == '>'):
            return b
        else:
            return


    else:

        if a_1 > b_1:
            e = a[0]
        elif a_1 == b_1:
            if a[0][0] == '(':
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


    if e[1:] == f[:-1]:
        if e[0] == '<' and f[-1] == '>':
            return e[1:]
        else:
            return

    return [e,f]

przedzial = data[0]
for i in range(1, len(data)):
    c = common_part(przedzial, data[i])
    if c != ';' and c != '' and c != None:
        przedzial = c
    else:
        przedzial = ['posty']
        break

print(*przedzial, sep=';')