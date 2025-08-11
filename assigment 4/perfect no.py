num = int(input("enter thenumber:"))
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print(f"{num} is perfect number:")
else:
    print(f"{num} is not a perfect number:")