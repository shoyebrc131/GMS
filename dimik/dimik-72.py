from math import sqrt
repeat = int(input())
for x in range(repeat):
    a, b, c = map(int, input().split())
    try:
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        print("%.2f" % area)
    except ValueError:
        print('Oh, No!')
