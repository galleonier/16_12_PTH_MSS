n = int(input())
numbers = list(map(int, input().split()))
sums = [numbers[i] + numbers[i + 1] for i in range(n - 1)]
print(" ".join(map(str, sums)))
