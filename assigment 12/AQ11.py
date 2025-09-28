text = input("Enter a string: ")


result = ""
for char in text:
    if char == " ":
        result += "-"   
    else:
        result += char


print("String after replacing spaces with hyphens:", result)