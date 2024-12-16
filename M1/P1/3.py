n = int(input())
arr = [int(input()) for _ in range(n)]

max1 = max(arr)
arr.remove(max1)
max2 = max(arr)

print(max1, max2)

