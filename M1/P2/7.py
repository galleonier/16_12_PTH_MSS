text = input().split()
articles = {'a', 'an', 'the', 'A', 'An', 'The'}
count = sum(1 for word in text if word in articles)
print(count)
