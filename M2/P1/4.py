total_sum = 0

with open('../Data/nums.txt', 'r', encoding='utf-8') as file:
    content = file.read()

numbers = re.findall(r'\d+', content)

total_sum = sum(map(int, numbers))

print(total_sum)
