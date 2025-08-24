def countdigit(num):
    if num == 0:
      return 0
    return 1 + countdigit(num//10)

def calculatesum(num,count):
   if num == 0:
      return 0
   digit = num % 10
   return (digit*count) + calculatesum(num//10, count)

def checkarmstrong(num):
   count = countdigit(num)
   total = calculatesum(num,count)
   return total == num

num = int(input("enter the number:"))  
if checkarmstrong(num):
   print(f"{num},is an armstomg number")

else:

   print(f"{num},is an not armstong number")


   