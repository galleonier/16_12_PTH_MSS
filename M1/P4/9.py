encrypted_word = input().strip()
n = int(input())

letter_freq = {}
for _ in range(n):
    letter, freq = input().split(": ")
    letter_freq[letter] = int(freq)

sorted_freq = sorted(letter_freq.items(), key=lambda item: item[1])
decoded_word = ''.join([item[0] for item in sorted_freq])

print(decoded_word)
