import string

def validate_password(pw):
    if len(pw) < 8:
        return False
    has_upper = any(c.isupper() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in string.punctuation for c in pw)
    return has_upper and has_digit and has_special

# Test
print(validate_password("Passw0rd!"))  # True
print(validate_password("password"))   # False
