from sys import stdin, stdout
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
            return str(eval(out))


repeat = int(stdin.readline())
for x in range(repeat):
    instr = stdin.readline()
    while not instr[:-1].endswith("=") :
        instr = instr + " " + stdin.readline()
    stdout.write(parser(instr)+ "\n")
