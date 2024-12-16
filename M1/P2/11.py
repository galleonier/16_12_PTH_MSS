import string
text = input().lower()
text = ''.join([char if char not in string.punctuation else ' ' for char in text])
words = set(text.split())
print(len(words))
