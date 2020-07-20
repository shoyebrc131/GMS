repeat = int(input())
for i in range(repeat):
    x = int(input())
    for j in range(x):
        print("*" * x)
    if not i + 1 == repeat:
        print()
