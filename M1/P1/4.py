nums = map(int, input().split())
if all(num % 2 == 0 for num in nums):
    print("Все четные")
else:
    print("Не все четные")
