text = input("Enter a string: ")
n = int(input("Enter the index to remove: "))


if 0 <= n < len(text):
    
    result = text[:n] + text[n+1:]
    print("Modified string:", result)
else:
    print("Invalid index!")