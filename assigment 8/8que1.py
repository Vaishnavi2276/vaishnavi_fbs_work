def area_of_reactangle(length, breadth):
    
    return  length * breadth
    


l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))


area = area_of_reactangle(l, b)

print(f"The area of the rectangle is: {area}")
