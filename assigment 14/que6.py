def max_product_pair(numbers):
    
    num_set = set(numbers)
    if len(num_set) < 2:
        return None, None, None
    nums = sorted(num_set)
    max1, max2 = nums[-1], nums[-2]
    min1, min2 = nums[0], nums[1]

    product1 = max1 * max2
    product2 = min1 * min2

    if product1 >= product2:
        return max1, max2, product1
    else:
        return min1, min2, product2



numbers = [2, 3, -5, -7, 4, 9, -6]
a, b, product = max_product_pair(numbers)

print("The two numbers are:", a, "and", b)
print("Maximum product is:", product)