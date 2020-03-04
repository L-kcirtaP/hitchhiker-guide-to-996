def fibonacci(n):
    return 1 if n == 0 or n == 1 else fibonacci(n-1) + fibonacci(n-2)
