repeat = int(input())
for x in range(repeat):
    out = (sorted(list(map(int, input().split()))))
    print("Case {y}:".format(y=x + 1), out[0], out[1], out[2])
