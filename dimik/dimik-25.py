repeat = int(input())
for x in range(repeat):
    innums = input().split()
    large = max(int(innums[0]), int(innums[1]))
    small = min(int(innums[0]), int(innums[1]))
    for i in range(0, small):
        if (large * (i + 1)) % small == 0:
            print("LCM =", large * (i + 1))
            break
