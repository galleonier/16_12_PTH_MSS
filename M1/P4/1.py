n = int(input())
countries = {}

for _ in range(n):
    data = input().split()
    country = data[0]
    cities = data[1:]
    for city in cities:
        countries[city.lower()] = country

m = int(input())
for _ in range(m):
    city = input().strip().lower()
    print(countries.get(city, "Неизвестно"))
