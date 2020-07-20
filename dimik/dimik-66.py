find = input()
replace = input()
print(replace)
print(find)
findandreplace = dict(zip(list(find), (replace)))
while True:
    try:
        txt = input()
        for i in txt:
            if i in findandreplace.keys():
                txt = txt.replace(i, findandreplace[i])
        print(txt)
    except EOFError:
        break
