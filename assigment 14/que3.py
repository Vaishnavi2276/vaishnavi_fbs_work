lines = [
    "Python is easy,to undastad"
    "I love learning Python",
    "Python is powerful and easy"
]

all_words = []
for line in lines:
    words = line.split()
    all_words.extend(words)


unique_words = set(all_words)

print("Unique words and their frequencies:")
for word in unique_words:
    print(word, ":", all_words.count(word))