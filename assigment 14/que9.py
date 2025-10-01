def find_triplets(numbers, target):
    triplets = []

    for combo in combo(numbers, 3):
        if sum(combo) == target:
            triplets.append(combo)
    
    return triplets



numbers = [1, 2, 3, 4, 5, 6]
target = 10

result = find_triplets(numbers, target)

print("Triplets with sum", target, ":")
for triplet in result:
    print(triplet)
