numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = []
odd_numbers = []


for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)  
    else:
        odd_numbers.append(num)   


print("Original List:", numbers)
print("Even Numbers List:", even_numbers)
print("Odd Numbers List:", odd_numbers)