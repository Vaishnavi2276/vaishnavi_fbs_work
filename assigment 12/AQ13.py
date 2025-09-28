def find_length(s):
    count = 0
    for _ in s:   
        count += 1
    return count


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


len1 = find_length(str1)
len2 = find_length(str2)


if len1 > len2:
    print("Larger string is:", str1)
elif len2 > len1:
    print("Larger string is:", str2)
else:
    print("Both strings are of equal length.")