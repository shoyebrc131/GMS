repeat = int(input())
for i in range(repeat):
    a = int(input())
    if a**(1 / 2) == int(a**(1 / 2)):
        print("YES")
    else:
        print("NO")
