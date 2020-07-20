repeat = int(input())
for x in range(repeat):
    listlen = int(input())
    print(" ".join(input().split()[0:listlen + 1:2]))
