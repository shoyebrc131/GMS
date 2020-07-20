def bs( y):
    n = 65
    L = 0
    R = 64
    while L <= R:
        mid = int((L+R)/2)
        if primelist[mid] < y:
            L = mid + 1
        elif primelist[mid] > y:
            R = mid - 1
        else:
            return True
    return False
def div(y):
    for k in primelist:
        if y%k ==0 and k !=y:
            return False
    return True
primelist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313]
repeat = int(input())
for x in range(repeat):
    count= 0
    a, b = map(int, input().split())
    if a==1:
        count+=1
        a = 3
    if a%2 == 0 :
        a = a+1
    for i in range(a, b + 1, 2):
        if bs(i) or div(i):
            count += 1
    print(count)
