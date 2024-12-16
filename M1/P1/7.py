import math

a, b = map(int, input().split())
while(a!=b+1):
    ch = True
    item = a
    for checked in range(2, ((item))):
        if(item%checked==0):
            ch = False
    if ch:
        print(item)
    a+=1
