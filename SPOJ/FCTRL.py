repeat = int(input())
x = 0
y = 1
z = 0
for i in range(repeat):
    x = int(input())
    while x / (5**y) > 0:
        z = z + int(x / (5**y))
        y = y + 1
    print(z)
    y = 1
    z = 0
