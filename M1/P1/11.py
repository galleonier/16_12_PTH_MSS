string = input()
CharB = ('А','В','Е')
if len(string)>=8 and len(string)<=9:
    if(string[0] in CharB and string[1].isnumeric() and string[2].isnumeric() and string[3].isnumeric() and string[4] in CharB and string[5] in CharB and string[6].isnumeric() and string[7].isnumeric() and string[-1].isnumeric()):
        print("YES")
else:
    print("NO")