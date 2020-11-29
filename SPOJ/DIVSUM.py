repeat = int(input())
x = 0
out = 0
for i in range(repeat):
    tmp = int(input())
    while tmp != 0:
        tmp //=5
        out +=tmp
    print(out)
    out = 0
