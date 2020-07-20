repeat = int(input())
for x in range(repeat):
    instrlst = list(input())
    unialphalist = sorted(set(instrlst))
    for i in unialphalist:
        if i.isalpha():
            print(i,"=",instrlst.count(i))
    if x < repeat -1:
        print()
