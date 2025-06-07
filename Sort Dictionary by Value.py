def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

# Test
print(sort_dict_by_value({'a': 3, 'b': 1, 'c': 2}))  # {'a': 3, 'c': 2, 'b': 1}
