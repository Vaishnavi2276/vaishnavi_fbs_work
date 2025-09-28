def three_sum(nums, target):
    nums.sort()  
    result = set()
    n = len(nums)

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    
    return list(result)



numbers = [1, 2, -1, 0, -2, 1, -1, 4]
target = 2

triplets = three_sum(numbers, target)
print("Unique triplets with sum", target, "are:")
for t in triplets:
    print(t)