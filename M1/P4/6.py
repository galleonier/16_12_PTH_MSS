identifiers = input().split()
counter = {}

for i in range(len(identifiers)):
    if identifiers[i] in counter:
        counter[identifiers[i]] += 1
        identifiers[i] = f"{identifiers[i]}_{counter[identifiers[i]]}"
    else:
        counter[identifiers[i]] = 0

print(" ".join(identifiers))
