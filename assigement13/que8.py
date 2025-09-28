text = input("Enter a string: ")

words = text.split()


freq = {}
for word in words:
    word = word.lower()   
    freq[word] = freq.get(word, 0) + 1


print("Word Frequency Dictionary:")
print(freq)