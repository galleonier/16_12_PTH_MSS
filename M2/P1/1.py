total_cost = 0

with open('../Data/prices.txt', 'r', encoding='utf-8') as file:
    for line in file:
        product_info = line.strip().split('\t')
        quantity = int(product_info[1])
        price_per_unit = int(product_info[2])
        total_cost += quantity * price_per_unit

print(f"Общая стоимость заказа: {total_cost} рублей")
