import string

def clean_string(s):
    return ''.join(ch.lower() for ch in s if ch in string.ascii_letters)

sentence1 = input().strip()
sentence2 = input().strip()

if sorted(clean_string(sentence1)) == sorted(clean_string(sentence2)):
    print("YES")
else:
    print("NO")
