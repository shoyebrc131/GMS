repeat = int(input())
for x in range(repeat):
    length, format = map(int, input().split())
    format = str(format)
    length = length -1
    for i in range(2*length+1):
        if i<length :
            print(i*(format + ' ') ,end="")
            print(format)
        else:
            print((length-(i-length))*(format + ' ') ,end="")
            print(format)
    print()
