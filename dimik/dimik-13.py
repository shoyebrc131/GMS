from math import factorial


repeat = int(input())
for x in range(repeat):
    inwdlist = input().split()
    uni_wd = set(inwdlist)
    divisor  = 1
    for i in uni_wd:
        divisor *= factorial(inwdlist.count(i))
    print("1/"+str(factorial(len(inwdlist))//divisor))