vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
repeat = int(input())
for x in range(repeat):
    instr = list(input())
    for j in instr:
        if j in vowels:
            print(j, end="")
    print()
    for j in instr:
        if j not in vowels and j != " " and j.isalpha():
            print(j, end="")
    print()
