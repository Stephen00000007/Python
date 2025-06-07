def count_extensions(filenames):
    ext_count = {}
    for file in filenames:
        ext = file.split('.')[-1]
        ext_count[ext] = ext_count.get(ext, 0) + 1
    return ext_count

# Test
files = ['a.txt', 'b.jpg', 'c.txt', 'd.png', 'e.jpg']
print(count_extensions(files))  # {'txt': 2, 'jpg': 2, 'png': 1}
