def reverse_each_word(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

# Test
print(reverse_each_word("Hello World"))  # olleH dlroW
