from math import log2


repeat = int(input())
for x in range(repeat):
    innum = int(input())
    if innum != 0:
        log = log2(innum)
        if innum == int(innum):
            print("It's a power of 2")
        else:
            print("Not a power of 2")
    else:
        print("Not a power of 2")
