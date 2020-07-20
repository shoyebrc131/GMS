def parser(lst):
    out = ""
    for i in lst:
        if i.isdigit():
            out += i
        elif i in ["*", "-", "+"]:
            out = str(eval(out)) + f" {i} "
        elif i == "/":
            out = str(eval(out)) + " // "
        elif i == "=":
            return int(eval(out))


repeat = int(input())
for x in range(repeat):
    instr = input()
    while not instr.endswith("=") :
        instr = instr + " " + input()
    print(parser(instr))
