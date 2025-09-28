n = int(input("Enter how many elements you want in the list: "))

numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)


result = [x for x in numbers if x % 2 != 0]


print("Original List:", numbers)
print("List after removing even numbers:", result)