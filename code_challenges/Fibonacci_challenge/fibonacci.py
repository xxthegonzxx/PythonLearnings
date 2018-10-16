# Method using recursion
def fib(n):
    # F(n) = F(n - 1) + F(n - 2)
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


# Much faster result, not using recursion
def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

for i in range(36):
    print(i, fibonacci(i))
