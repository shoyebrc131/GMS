instr = input()
deviate = int(input())
for x in instr:
    if x.isalpha():
        uni = ord(x)
        if x.islower():
            x = chr(97 + ((uni + deviate) - 97) % 26)
        elif x.isupper():
            x = chr(65 + ((uni + deviate) - 65) % 26)
    print(x, end="")
print()
