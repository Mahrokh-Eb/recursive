# factorial - Recursive function
def factorial(x):
    if x <= 1:
        return x
    else:
        return x * factorial(x - 1)


print(factorial(9))

print(factorial(3))


# Fibonacci - recursive function : 0, 1, 1, 2, 3, 5, 8, 13...
def fibonacci(y):
    if y == 0:
        return 0
    elif y == 1:
        return 1
    else:
        return fibonacci(y - 1) + fibonacci(y - 2)


n = fibonacci(5)
print(n)
