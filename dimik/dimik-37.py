repeat = int(input())
wordlist = []
for x in range(repeat):
    wordlist.append(input())
wordlist =sorted(wordlist)
for i in wordlist:
    print(i)
