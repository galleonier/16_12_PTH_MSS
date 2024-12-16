n = int(input())
phonebook = {}

for _ in range(n):
    phone, name = input().split()
    name = name.lower()
    if name in phonebook:
        phonebook[name].append(phone)
    else:
        phonebook[name] = [phone]

m = int(input())
for _ in range(m):
    query = input().strip().lower()
    if query in phonebook:
        print(" ".join(phonebook[query]))
    else:
        print("абонент не найден")
