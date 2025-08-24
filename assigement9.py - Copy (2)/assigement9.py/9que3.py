def revercenumber(n,rev):
    if n == 0:
        return rev
    
    rev = (rev * 10) + (n % 10)
    return reverse_number (n // 10, rev)

num = int(input("enter the number:"))
reversed_num = reverse_number(num)

print("reversed number:", reversed_num)