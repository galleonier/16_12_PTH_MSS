def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    return sum(1 for a, b in zip(word1, word2) if a != b) == 1

print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
print(is_one_away('aab', 'aba'))
