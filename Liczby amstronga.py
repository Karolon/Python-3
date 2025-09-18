amstrongNumbers3 = []
amstrongNumbers = []
lengList = [0]*9
for i in range(1,1000001):
    number = i
    length = 0
    while number != 0:
        number //= 10
        length += 1


    number = i
    digitSum = 0
    for j in range(length):
        digitSum += (number % 10) ** length
        number //= 10

    if digitSum == i:
        amstrongNumbers.append(i)
        lengList[length] += 1
        if length == 3:
            amstrongNumbers3.append(i)

print(amstrongNumbers)
for i in range(9):
    print(f'{i+1}: {lengList[i]}')

for n in amstrongNumbers:
    binary = bin(n)[2:]
    if binary == binary[::-1]:
        print(n)

#
# for n in amstrongNumbers:
#     for m in amstrongNumbers:
#         for nm in amstrongNumbers:
#             if nm == n + m:
#                 print(nm, n, m)