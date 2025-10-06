divisors = range(1, 10)

numbers = [n for n in range(1, 1001) if any(n % d == 0 for d in divisors)]

print(numbers)
