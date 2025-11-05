def fibonaci(n):
    if n == 1 or n == 0:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)

def factorial(n):
    if n == 0:
        return 1
    if n == 2:
        return 2
    return factorial(n-1) * n

def power(n, a):
    if a == 0:
        return 1
    return  power(n, a-1) * n

def power2(n, a):
    if a == 0:
        return 1
    if a == 1:
        return n
    if a == -1:
        return 1/n
    return  power2(n, a//2) * power2(n, a-(a//2))

print(fibonaci(4))
print(factorial(8))
print(power2(-10, -5))