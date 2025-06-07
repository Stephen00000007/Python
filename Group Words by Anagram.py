def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

# Test
print(group_anagrams(["bat", "tab", "cat", "act", "tac"]))  
# [['bat', 'tab'], ['cat', 'act', 'tac']]
