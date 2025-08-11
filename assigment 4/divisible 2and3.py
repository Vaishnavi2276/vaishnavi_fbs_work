n = int(input("enter the value of n:"))
print(f"integer up to {n} that divisible by 2 or 3:")
for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 !=0:
        print(i, end=" ")