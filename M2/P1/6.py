count = 0

with open('../Data/grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        surname, grade1, grade2, grade3 = line.split()
        if int(grade1) >= 65 and int(grade2) >= 65 and int(grade3) >= 65:
            count += 1

print(count)