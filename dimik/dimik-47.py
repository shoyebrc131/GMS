repeat = int(input())
for x in range(repeat):
    n1 = list(map(int, input().split()))[1:]
    n2 = list(map(int, input().split()))[1:]
    n3 = sorted(n1 + n2)
    print(" ".join(list(map(str, n3))))
