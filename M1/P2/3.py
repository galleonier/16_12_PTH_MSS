n = int(input())
negatives = []
zeros = []
positives = []

for _ in range(n):
    number = int(input())
    if number < 0:
        negatives.append(number)
    elif number == 0:
        zeros.append(number)
    else:
        positives.append(number)

print("\n".join(map(str, negatives)))
print("\n".join(map(str, zeros)))
print("\n".join(map(str, positives)))