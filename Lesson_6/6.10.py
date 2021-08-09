# 6.10 exercise fibonacci
def recur_fibo(n):
    if n <= 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
        # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b