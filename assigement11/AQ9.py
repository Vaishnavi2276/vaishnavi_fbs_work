n = int(input("Enter how many numbers you want: "))


numbers = []
squares = []
cubes = []

for i in range(1, n+1):
    numbers.append(i)
    squares.append(i ** 2)
    cubes.append(i ** 3)


print("Numbers List:", numbers)
print("Squares List:", squares)
print("Cubes List:", cubes)