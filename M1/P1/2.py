n = int(input())
total_sum = 0
for i in range(1, n + 1):
    square = i ** 2
    if square % 10 in [2, 5, 8]:
        total_sum += i
print(total_sum)
