repeat = int(input())
for x in range(repeat):
    uplim = int(input())
    for i in range(uplim, -1, -1):
        if i > 1:
            print("2^{k} + ".format(k=i), end="")
        elif i == 1:
            print("2 + ", end="")
        else:
            print(1)
