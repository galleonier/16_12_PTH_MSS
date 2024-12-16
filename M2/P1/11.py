import csv

column_index = int(input()) - 1

with open('../Data/deniro.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

if rows[0][column_index].isdigit():
    rows.sort(key=lambda x: int(x[column_index]))
else:
    rows.sort(key=lambda x: x[column_index].lower())

for row in rows:
    print(','.join(row))