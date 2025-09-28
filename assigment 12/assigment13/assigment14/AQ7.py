from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)

    for word in words:
        
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)

    
    return list(anagram_groups.values())



words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)

print("Grouped Anagrams:")
for group in result:
    print(group)