with open('../Data/lines.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

max_len = max(len(line) for line in lines)

for line in lines:
    if len(line) == max_len:
        print(line, end='')
