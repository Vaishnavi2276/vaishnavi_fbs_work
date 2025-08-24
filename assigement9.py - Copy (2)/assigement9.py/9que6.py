def fibonacci(i):
    if(i <= 1):
        return i
    else:
        return fibonacci(i-1)+ fibonacci(i-2)
    
term = int(input("enter the tearm of fibonacci serious:"))
for i in range(0, term):
    print(fibonacci(i))


    