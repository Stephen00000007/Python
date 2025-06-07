from collections import Counter

def frequency_count(lst):
    return dict(Counter(lst))

# Test
print(frequency_count(['a', 'b', 'a', 'c', 'b', 'a']))  # {'a': 3, 'b': 2, 'c': 1}
