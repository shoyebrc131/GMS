from math import sqrt,floor
def factorsum(x):
    sum =1
    xsqrt = int((x)**(0.5)) +1
    for j in range(2, xsqrt):
        if x % j == 0:
            sum = sum + j + x//j
    return sum


repeat = int(input())
for i in range(repeat):
    y = int(input())
    if factorsum(y) == y:
        print('YES,', y, 'is a perfect number!')
    else:
        print('NO,',y, 'is not a perfect number!')
