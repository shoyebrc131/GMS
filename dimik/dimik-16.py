repeat = int(input())
for x in range(repeat):
    inlist = input().split()
    for i in range(len(inlist) - 1):
        print(inlist[i][::-1], end=" ")
    print(inlist[-1][::-1])
