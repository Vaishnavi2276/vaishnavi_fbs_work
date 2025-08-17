
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total

n = 10
print("Sum of all odd numbers from 1 to", n, "is:", sum_of_odds(n))