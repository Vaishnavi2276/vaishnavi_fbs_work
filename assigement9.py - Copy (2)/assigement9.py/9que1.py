def factorial(num):
   if num == 0 or num == 1:
    return 1
   else:
    return num * factorial(num-1)

def sumofdigit(n):

    if n == 0:
       return 0
    else:
       return factorial(n)+sumofdigit(n-1)

n = int(input("enter the number:"))

result = sumofdigit (n)
print(f"sum of serious 1!+2!+3!+....{n}={result}") 

