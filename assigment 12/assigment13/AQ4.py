n = int(input("Enter the value of n: "))


square_dict = {}
for x in range(1, n + 1):
    square_dict[x] = x * x


print("Generated Dictionary:", square_dict)