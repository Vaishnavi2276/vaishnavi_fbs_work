str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


if sorted(str1.replace(" ", "")) == sorted(str2.replace(" ", "")):
    print("Yes! The strings are anagrams.")
else:
    print("No! The strings are not anagrams.")