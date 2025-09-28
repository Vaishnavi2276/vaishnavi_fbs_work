int = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in int:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)