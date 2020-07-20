dictlen, descno = map(int, input().split())
salarydict = dict()
dictkey = list()
for i in range(dictlen):
    x, y = input().split()
    salarydict[x] = int(y)
    dictkey.append(x)
for j in range(descno):
    desc = str()
    salary = 0
    while True:
        desc = input()
        descl = desc.split()
        for k in descl:
            if k in dictkey:
                salary = salary + salarydict[k]
        if desc.endswith("."):
            break
    print(salary)
