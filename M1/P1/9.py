string = input()
fin = 0
for i in string:
    if i.isnumeric():
        fin+=1
print(fin)