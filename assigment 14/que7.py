def find_missing(set1, set2):
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1
    
    return missing_in_set2, missing_in_set1

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}

missing_in_set2, missing_in_set1 = find_missing(set1, set2)

print("Numbers in set1 but missing in set2:", missing_in_set2)
print("Numbers in set2 but missing in set1:", missing_in_set1)