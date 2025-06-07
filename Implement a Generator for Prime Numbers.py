def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    for num in range(2, n):
        if is_prime(num):
            yield num

# Test
print(list(prime_generator(20)))  # [2, 3, 5, 7, 11, 13, 17, 19]
