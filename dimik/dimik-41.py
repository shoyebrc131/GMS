from math import factorial
repeat = int(input())
for x in range(repeat):
    uplim = int(input())
    out = 0
    for i in range(uplim):
        out = out + 1 / factorial(i)
    print("%.4f" % out)
