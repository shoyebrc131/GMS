repeat = int(input())
for x in range(repeat):
    alphalist = list(input())
    for i in alphalist:
        print(ord(i) - 64, end="")
    print()
