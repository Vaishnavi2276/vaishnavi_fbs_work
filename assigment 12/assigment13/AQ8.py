text = input("Enter a string: ")


text = text.lower()


words = text.split()


freq_dict = {}

for word in words:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1


print("Word Frequencies:", freq_dict)