def asciihash(x):
    hash = 1
    letlist = list(x)
    for i in letlist:
        hash = hash*ord(i)
    return hash%97

repeat = int(input())
for x in range(repeat):
    y = input().split()
    if asciihash(y[0]) == asciihash(y[1]):
        print("YES")
    else:
        print("NO")
