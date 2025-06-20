def is_clean_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Test
print(is_clean_palindrome("A man, a plan, a canal: Panama"))  # True
