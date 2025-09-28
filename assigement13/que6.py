numbers = {
    "a": 33,
    "b": 44,
    "c":55
}

print("Dictionary:", numbers)


result = 1
for value in numbers.values():
    result *= value
print("Multiplication of all items in the dictionary:", result)