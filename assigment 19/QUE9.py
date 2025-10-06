def palindrome_generator():
    """Infinite generator that yields palindrome numbers."""
    n = 0
    while True:
        if str(n) == str(n)[::-1]: 
            yield n
        n += 1

pal_gen = palindrome_generator()

print("First 20 palindrome numbers:")
for _ in range(20):
    print(next(pal_gen), end=" ")