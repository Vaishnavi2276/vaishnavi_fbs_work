from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)
    
    for word in words:
    
        key = ''.join(sorted(word))
        anagram_dict[key].append(word)
    

    return list(anagram_dict.values())


words = ["listen", "silent", "enlist", "hello", "ohlle", "world", "dworl"]

groups = group_anagrams(words)

print("Grouped Anagrams:")
for group in groups:
    print(group)