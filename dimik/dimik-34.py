repeat = int(input())
for x in range(repeat):
    div1, div2, uplim = map(int, input().split())
    divisor = div1 * div2
    for i in range(divisor, uplim + 1, divisor):
        print(i)
    if x != repeat - 1:
        print()
