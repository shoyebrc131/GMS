repeat = int(input())
for x in range(repeat):
    x, k = map(int, input().split())
    out = 1
    for i in range(k):
        out += x**(i + 1)
    print("Result =", out)
