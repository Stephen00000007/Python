def remove_consecutive_duplicates(s):
    result = [s[0]] if s else []
    for char in s[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)

# Test
print(remove_consecutive_duplicates("aaabbcdddda"))  # abcd a
