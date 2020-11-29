def prime(i):
    if i == 1:
        return False
    if i == 2:
        return True
    if i%2 ==0 :
        return False
    j = 3
    while j*j <= i:
        if i%j == 0:
            return False
        j +=2
    return True

repeat = int(input())
for x in range(repeat):
    inint = int(input())
    if not prime(inint):
        print(inint, "is not a prime")
    else :
        print(inint, "is a prime")
