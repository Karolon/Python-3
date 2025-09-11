file = open("folder/dane2.txt")

for f in file:
  dane = str(f.strip())

ilośc_liczb = 0
lista_liczb = list(map(str, [1,2,3,4,5,6,7,8,9,0]))
for i in range(len(dane)):
  if dane[i] in lista_liczb and dane[i+1] not in lista_liczb:
    ilośc_liczb += 1
    
print(ilośc_liczb)


biggest = [0,0]
for i in range(10):
  cyfra = dane.count(chr(48+i))
  if cyfra > biggest[0]:
    biggest = [cyfra, i]

print(biggest[::-1])