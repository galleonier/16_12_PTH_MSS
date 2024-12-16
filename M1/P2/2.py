n = int(input())
seen = set()
unique_lines = []

for _ in range(n):
    line = input()
    if line not in seen:
        seen.add(line)
        unique_lines.append(line)
print("\n".join(unique_lines))
