def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m,n-1)
    
m = int(input("enter the number(m):"))
n = int(input("enter the number(n):"))

result = power(m,n)
print(f"{m} to the power{n} is:{result}")

    

