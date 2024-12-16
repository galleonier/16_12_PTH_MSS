with open('../Data/class_scores.txt', 'r', encoding='utf-8') as file:
    for line in file:
        surname, score = line.split()
        new_score = min(int(score) + 5, 100)
        print(f"{surname} {new_score}")