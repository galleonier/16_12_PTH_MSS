count = 0

with open('../Data/sales.csv', 'r', encoding='utf-8') as file:
    for line in file:
        name, old_price, new_price = line.strip().split(';')
        if int(new_price) < int(old_price):
            count += 1

print(count)