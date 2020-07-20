repeat = int(input())
for x in range(repeat):
    instr = input()
    letter = input()
    occurence = instr.count(letter)
    if occurence == 0:
        print("\'{l}\' is not present".format(l=letter))
    else:
        print("Occurrence of \'{l}\' in \'{str}\' = {o}".format(
            l=letter, str=instr, o=occurence))
