#sito eratostenesa
import time

startt = time.time()

sito = [True]*10000001
sito[0] = False
sito[1] = False

prime = []
for i in range(3, len(sito), 2):
  if sito[i]:
    for j in range(i**2, len(sito), i):
      sito[j] = False
    prime.append(i)

print(time.time() - startt)
print(prime)


