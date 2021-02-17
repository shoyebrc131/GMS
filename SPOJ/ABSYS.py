repeat = int(input())
for x in range(repeat):
    a, x, b, y, c = input().split()
    if a.isdigit() and b.isdigit():
        print(f'{a} + {b} = {int(a) + int(b)}')
    elif b.isdigit() and c.isdigit():
        print(f'{int(c) - int(b)} + {b} = {c}')
    elif a.isdigit() and c.isdigit():
        print(f'{a} + {int(c) - int(a)} = {c}')
