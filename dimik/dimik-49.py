def prime(i):
    if i < 2:
        return False
    j = 2
    while j*j <= i:
        if i%j == 0:
            return False
        j +=j
    return True

repeat = int(input())
for x in range(repeat):
    inint = int(input())
    if not prime(inint) or inint :
        print(inint, "is not a prime")
    else :
        print(inint, "is a prime")
