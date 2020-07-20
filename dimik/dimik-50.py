repeat = int(input())
for x in range(repeat):
    strlist = list(input())
    for i in range(len(strlist)):
        if strlist[i] == "R":
            strlist[i] = strlist[i+1]
        elif strlist[i]=="L":
            strlist[i] = strlist[i-1]
    print("".join(strlist))
