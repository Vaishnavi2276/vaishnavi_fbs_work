list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]


union_list = list(set(list1) | set(list2))

print("List 1:", list1)
print("List 2:", list2)
print("Union of the lists:", union_list)