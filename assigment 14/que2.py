set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Original set1:", set1)
print("Original set2:", set2)


set1 -= set1.intersection(set2)

print("Set1 after removing intersection with set2:", set1)