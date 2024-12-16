text = input().split()
result = []
current_char = text[0]
current_group = []
for word in text:
    for char in word[0]:
        if char == current_char:
            current_group.append(char)
        else:
            result.append(current_group)
            current_group = [char]
            current_char = char
result.append(current_group)
print(result)
