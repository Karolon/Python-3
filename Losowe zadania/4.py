file = open("dane/slowa.txt")

data = [f.strip() for f in file]

print(sum(d == d[::-1] for d in data))

palindrome_families = set()
for d in data:
    if d == d[::-1]:
        palindrome_families.add(len(d))

palindrome_family = []
for i in range(max([len(d) for d in data])):
    palindrome_family.append([])
for d in data:
    if d == d[::-1]:
        palindrome_family[len(d)-1].append(d)
print(len(palindrome_families))


file_ans = open('rodziny.txt', 'w')
print(*[sorted(p) for p in palindrome_family], file = file_ans, sep='\n')