def find_pairs(numbers, target_sum):
    pairs = []
    n = len(numbers)
    
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] == target_sum:
                pairs.append((numbers[i], numbers[j]))
    return pairs

numbers = [2, 4, 3, 7, 5, 8, 1]
target_sum = 9

result = find_pairs(numbers, target_sum)
print("Pairs with sum", target_sum, ":", result)