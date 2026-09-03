def fibonacci(n):
    fib = []
    a, b = 0, 1

    for i in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

# Example
print(fibonacci(7))
# Output: [0, 1, 1, 2, 3, 5, 8]
