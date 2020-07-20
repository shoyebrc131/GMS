repeat = int(input())
for i in range(repeat):
    y = list(map(int, input().split()))
    b = (y[0] + 1 - y[1]) / (y[2] / 6)
    if y[1] > y[0]:
        b = 0.00
    print("{:.2f} {:.2f}".format(y[1] / ((300 - y[2]) / 6), b))
