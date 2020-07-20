vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
out = 0
repeat = int(input())
for x in range(repeat):
    instr = input()
    for n in range(len(instr)):
        if instr[n] in vowels:
            out = out + 1
    print('Number of vowels =', out)
    out = 0
