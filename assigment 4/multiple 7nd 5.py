teamp1 = int(input("enter the teamp1 of the range:"))
teamp2 = int(input("enter the teamp2 of the range:"))
print(f"number divisible by 7 and multiple of between {teamp1} and {teamp2}:")
for num in range(teamp1, teamp2 + 1):
    if num % 7 == 0 and num % 5 == 0:
        print(num)