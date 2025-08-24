def sum_n(n):
    if n == 0:
        return 0
    else:
     return n + sum_n(n-1)

n = int(input("enter the number:"))
print("sum of first", n, "number is:",sum_n(n))

    
    