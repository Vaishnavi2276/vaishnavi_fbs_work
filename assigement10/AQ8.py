numbers = [10, 20, 30, 40, 50]


duplicate1 = numbers[:]
print("Duplicate list:", duplicate1)


duplicate2 = list(numbers)
print("Duplicate list:", duplicate2)


duplicate3 = numbers.copy()
print("Duplicate list :", duplicate3)


print("Are original and duplicate1 same object?", numbers is duplicate1)
print("Are original and duplicate2 same object?", numbers is duplicate2)
print("Are original and duplicate3 same object?", numbers is duplicate3)