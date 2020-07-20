repeat = int(input())
for x in range(repeat):
    innum, limiter = input().split()
    innum, limiter = int(innum), int(limiter)
    if limiter < innum:
        print("Invalid!")
    for x in range(1, int(limiter / innum) + 1):
        print(x * innum)
    print()
