from collections import defaultdict

company_salaries = defaultdict(list)

with open('../Data/salary_data.csv', 'r', encoding='utf-8') as file:
    for line in file:
        company, salary = line.strip().split(';')
        company_salaries[company].append(int(salary))

averages = [(company, sum(salaries) / len(salaries)) for company, salaries in company_salaries.items()]

averages.sort(key=lambda x: (x[1], x[0]))

for company, _ in averages:
    print(company)
