def find_pairs(numbers, target):
    pairs = []
    n = len(numbers)

    
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    
    return pairs



numbers = [2, 4, 3, 5, 7, 8, 9]
target = 10

result = find_pairs(numbers, target)

print(f"Pairs with sum :", result)