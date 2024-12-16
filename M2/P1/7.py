import re
with open('../Data/forbidden_words.txt', 'r', encoding='utf-8') as file:
    forbidden_words = set(file.read().strip().split())

with open('../Data/some_data.txt', 'r', encoding='utf-8') as file:
    content = file.read()

for word in forbidden_words:
    content = re.sub(rf'\b{word}\b', '*' * len(word), content, flags=re.IGNORECASE)

print(content)
