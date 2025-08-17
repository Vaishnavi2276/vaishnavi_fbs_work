def print_fibonacci(n):
    a, b = 1, 1 
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


n = int(input("Enter the number of terms: "))
print("Fibonacci series up to", n, "terms:")
print_fibonacci(n)