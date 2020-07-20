repeat = int(input())
for x in range(repeat):
    x, y = input().split()
    x, y =x[::-1] ,y[::-1]
    z = int(x)+int(y)
    print(int(str(z)[::-1]))
