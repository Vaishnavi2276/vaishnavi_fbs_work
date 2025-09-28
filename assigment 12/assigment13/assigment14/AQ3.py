lines = [
    "Python is great and Python is easy",
    "Learning Python is fun",
    "Sets are useful in Python"
]


words = []
for line in lines:
    words.extend(line.split())   


unique_words = set(words)


print("Unique words and their frequencies:")
for word in unique_words:
    print(word, ":", words.count(word))