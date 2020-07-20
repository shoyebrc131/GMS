repeat = int(input())
for x in range(repeat):
    inlist = list(map( int, input().split()))
    inlen = inlist.pop(0)
    avg = sum(inlist)//inlen
    inlist.sort()
    for i in range(inlen):
        if inlist[i] > avg:
            result = (inlen-i)/inlen *100
            break
        result = 0
    print("%.3f"%result, "%",sep="")
