with open('../Data/data.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line, end='')
