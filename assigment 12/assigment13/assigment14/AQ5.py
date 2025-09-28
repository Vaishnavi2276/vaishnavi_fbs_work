def max_product_pair(numbers):
    num_set = set(numbers)   
    
    
    nums = sorted(num_set)
    
    
    product1 = nums[-1] * nums[-2]
    product2 = nums[0] * nums[1]
    
    if product1 > product2:
        return (nums[-2], nums[-1]), product1
    else:
        return (nums[0], nums[1]), product2


numbers = [5, -10, -20, 7, 8, 9]
pair, product = max_product_pair(numbers)
print("Pair with maximum product:", pair)
print("Maximum product:", product)