x = int(input())
for j in range(x):
    q = int(input())
    print("Case", j + 1, end=": ")
    for t in range(1, int(q / 2 + 1)):
        if q % t == 0:
            print(t, end=" ")
    print(q)
