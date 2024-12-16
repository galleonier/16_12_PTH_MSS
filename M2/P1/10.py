from collections import defaultdict

domain_count = defaultdict(int)

with open('../Data/data.csv', 'r', encoding='utf-8') as file:
    for line in file:
        first_name, surname, email = line.strip().split(',')
        domain = email.split('@')[1]
        domain_count[domain] += 1

sorted_domains = sorted(domain_count.items(), key=lambda x: (x[1], x[0]))

print("domain\tcount")
for domain, count in sorted_domains:
    print(f"{domain}\t{count}")
