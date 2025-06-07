def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    v = c = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1
    return v, c

# Test
print(count_vowels_consonants("Hello World"))  # (3, 7)
