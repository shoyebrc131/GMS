repeat = int(input())
for x in range(repeat):
    instr = input()
    inint = int(instr)
    inlst = list(map(int, list(instr)))
    armed = sum(map(lambda x: x**3, inlst))
    print(armed)
    if armed == inint:
        print(instr, "is an armstrong number!")
    else:
        print(instr, "is not an armstrong number!")
