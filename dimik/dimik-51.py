repeat = int(input())
for x in range(repeat):
    instr, insubstr = input().split()
    print(instr.finds(insubstr))
