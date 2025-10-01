def longest_common_prefix(strings):
    if not strings:
        return ""

    shortest = min(strings, key=len)
    
    prefix = ""
    for i in range(len(shortest)):
    
        chars = {s[i] for s in strings}
        
        
        if len(chars) == 1:
            prefix += chars.pop()
        else:
            break
    return prefix



words = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longest_common_prefix(words))