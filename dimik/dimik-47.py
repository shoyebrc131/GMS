repeat = int(input())
for x in range(repeat):
    input()
    n1 = list(map(int,input().split()))
    input()
    n2 = list(map(int,input().split()))
    n3 =sorted(n1+n2)
    print(" ".join(list(map(str,n3))))
