from sys import stdin, stdout
repeat = int(stdin.readline())
x = 0
out = 0
for i in range(repeat):
    tmp = int(stdin.readline())
    while tmp != 0:
        tmp //=5
        out +=tmp
    stdin.write(str(out)+"\n")
    out = 0
