def spell(*args):
    result = {}
    for word in args:
        first_letter = word[0].lower()
        word_length = len(word)
        if first_letter not in result or word_length > result[first_letter]:
            result[first_letter] = word_length
    return result

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
