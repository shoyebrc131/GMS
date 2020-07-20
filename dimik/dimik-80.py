from math import gcd
while True:
    Oli , Stan = list(map(int,input().split()))
    if Oli==Stan ==0:
        break
    if gcd(Stan,Oli)%2:
        print("Stan wins")
    else:
        print("Ollie wins")
