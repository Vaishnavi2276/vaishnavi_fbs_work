int = input("Enter a string: ")


if len(int) > 1:
    new_string = int[-1] + int[1:-1] + int[0]
else:
    new_string = int 

print("New string:", new_string)