text = input().split()
squares = [str(int(num)**2) for num in text if int(num) % 2 == 0 and int(num)**2 % 10 != 4]
print(" ".join(squares))
