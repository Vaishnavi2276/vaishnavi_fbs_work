def fibonacci(limit):
    """Generator to yield Fibonacci numbers up to a given limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

limit = int(input("Generate Fibonacci numbers up to: "))

print(f"Fibonacci numbers up to {limit}:")
for num in fibonacci(limit):
    print(num, end=" ")