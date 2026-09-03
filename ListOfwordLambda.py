words = ["apple", "banana", "cat", "elephant", "python", "book"]

def word_lengths(words):
    return list(map(lambda x: len(x), words))


def long_words(words):
    return list(filter(lambda x: len(x) > 5, words))

def sort_words(words):
    return sorted(words, key=lambda x: len(x))


print("Length of words:", word_lengths(words))
print("Words with more than 5 characters:", long_words(words))
print("Words sorted by length:", sort_words(words))
