# import random as r
#
# data = sorted([r.randint(-500,5000) for i in range(r.randint(123,1024))])
#
# goal = 13
# indeks  = -1
#
# start = 0
# end = len(data)
# while end > start:
#     middle = (end + start) // 2
#     if goal == data[middle]:
#         indeks = middle
#         start = end
#     elif goal < data[middle]:
#         end = middle
#     else:
#         start = middle
#
# if index_ == -1:
#     print('Nie ma w liśćie')
# else:
#     print(indeks, data[indeks])



def BinarySearch(data, n):
    if n > data[-1]:
        return None
    start = 0
    end = len(data)
    indicator = 0
    while start < end:
        indicator = (start + end)//2
        if data[indicator] == n:
            return indicator
        elif n > data[indicator]:
            start = indicator
        else:
            end = indicator

    return None

