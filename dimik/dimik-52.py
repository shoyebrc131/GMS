repeat = int(input())
for x in range(repeat):
    instr, insubstr = input().split()
    ret = 0
    count = 0
    while True:
        ret = instr.find(insubstr, ret) + 1
        if ret == 0:
            break
        count += 1
    print(count)
