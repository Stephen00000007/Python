def find_missing_number(nums):
    n = len(nums) + 1
    return n * (n + 1) // 2 - sum(nums)

# Test
print(find_missing_number([1, 2, 4, 5]))  # 3