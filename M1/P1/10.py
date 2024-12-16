string = input()
f_i = string.find('f')
l_i = string.rfind('f')
if f_i == -1:
    print("NO")
elif f_i == l_i:
    print(f_i)
else:
    print(f_i, l_i)
