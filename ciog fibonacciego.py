
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    return  factorial(n-1) * n

print(factorial(int(input())))