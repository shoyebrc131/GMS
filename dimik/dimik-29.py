repeat = int(input())
for x in range(repeat):
    instr = input()
    if instr.isupper():
        print("Uppercase Character")
    elif instr.islower():
        print("Lowercase Character")
    elif instr.isnumeric():
        print("Numerical Digit")
    else:
        print("Special Character")
