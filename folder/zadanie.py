file = open("dane.txt")

dane = str(file)
ilośc_liczb = 0
for i in range(9):
  dane.count(chr(48+i))

print(dane)
