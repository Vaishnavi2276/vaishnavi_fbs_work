num = int(input("enter a number:"))
strong_num = num
sum_of_factorial = 0
while num > 0:
    digit = num % 10
    sum_of_factorial += factorial(digit)
    num //= 10

if sum_of_factorials == original_num:
    print(f"{strong_num}is a stong number")
else:
    print(f"{storng_num}is not strong number")