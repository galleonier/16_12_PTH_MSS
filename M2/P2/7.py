import numpy as np

def analyze_sales_data(sales_data):
    has_zero_sales = np.any(sales_data[:, 1] == 0)
    all_positive_income = np.all(sales_data[:, 2] > 0)
    return has_zero_sales, all_positive_income

sales_data_array = np.array([[1, 10, 100],
                             [2, 5, 50],
                             [3, 0, 0],
                             [4, 8, 80]])

has_zero_sales, all_positive_income = analyze_sales_data(sales_data_array)

print(f"Есть ли товары с нулевыми продажами: {has_zero_sales}")
print(f"Все ли товары имеют положительный доход: {all_positive_income}")
