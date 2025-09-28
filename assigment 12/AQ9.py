text = input("Enter a string: ")


words = text.split()
num_words = len(words)

num_chars = len(text.replace(" ", ""))

print("Number of words:", num_words)
print("Number of characters:", num_chars)
