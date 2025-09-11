file = open("dane maj 23/dron.txt")
cordinates = [[0,0]]
for f in file:
  x, y = f.split()
  x, y = map(int, [x,y])
  x += cordinates[-1][0]
  y += cordinates[-1][1]
  cordinates.append([x, y])

print(cordinates)
print("\n")
for point1 in cordinates:
  for point2 in cordinates:
    x1, y1 = point1
    x2, y2 = point2
    x3 = (x2 - x1)//2 + x1
    y3 = (y2 - y1)//2 + y1
    if [x3, y3] in cordinates and x1 != x2:
      print([x3, y3])