repeat = int(input())
for x in range(repeat):
    instr = input()
    if instr == instr[::-1]:
        print("Yes! It is Palindrome!")
    else:
        print("Sorry! It is not Palindrome!")
