def custom_sort(lst):
    return sorted(lst, key=lambda x: (-x[1], x[0]))

# Test
print(custom_sort([("Alice", 30), ("Bob", 25), ("Charlie", 30), ("Dave", 25)]))
# [('Alice', 30), ('Charlie', 30), ('Bob', 25), ('Dave', 25)]
