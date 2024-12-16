from collections import Counter

text = input().strip().lower()
words = text.split()

word_count = Counter(words)

rare_word = min(word_count, key=lambda word: (word_count[word], word))
print(rare_word)
