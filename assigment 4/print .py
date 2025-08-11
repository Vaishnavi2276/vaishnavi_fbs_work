teamp1 = int(input("enter the teamp1 of the range:"))
teamp2 = int(input("enter the teamp2 of the range:"))
divisor = int(input("enter the number to check divisiblity:"))

print(f"numbers divisible by {divisor} in the renge {teamp1} to {teamp2}:")

for num in range(teamp1,teamp2 + 1):
    if num % divisor == 0:
        print(num)