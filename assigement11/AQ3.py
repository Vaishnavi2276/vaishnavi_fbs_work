list_of_sublists = [[1, 3], [4, 1], [2, 2], [5, 0]]


sorted_list = sorted(list_of_sublists, key=lambda x: x[1])


print("Original List:", list_of_sublists)
print("Sorted List:", sorted_list)