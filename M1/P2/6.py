text = input().split()
numbers = list(map(int, text))

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
print(" ".join(map(str, numbers)))