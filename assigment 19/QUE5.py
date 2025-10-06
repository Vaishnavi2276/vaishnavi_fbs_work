text = input("Enter a string: ")

words = text.split()

short_words = [word for word in words if len(word) < 5]

print("Words with less than 5 letters:", short_words)
