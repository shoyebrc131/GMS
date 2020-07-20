repeat = int(input())
for x in range(repeat):
    lowlim, uplim, div = map(int, input().split())
    if lowlim % div == 0:
        divisible = lowlim
    else:
        divisible = (div - lowlim % div) + lowlim
    for i in range(divisible, uplim + 1, div):
        print(i)
    print()
