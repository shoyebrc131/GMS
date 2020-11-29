from math import sqrt
repeat = int(input())
for x in range(repeat):
    a,b,c = map(int,input().split())
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area = %.3f" %area)
