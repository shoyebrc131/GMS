checked = [6,28,496, 8128,33550336]
repeat = int(input())
for i in range(repeat):
    y = int(input())
    for d in checked:
        if d<=y:
            print(d)
    if i!=repeat-1:
        print()
