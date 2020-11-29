from sys import stdin, stdout
repeat = int(stdin.readline()[:-1])
for x in range(repeat):
    result = list()
    arr1 = list(map(int,stdin.readline()[1:-1].split()))
    arr2 = list(map(int,stdin.readline()[1:-1].split()))
    i,j =0,0
    while  i  < len(arr1) and j < len(arr2):
        if arr2[j] < arr1[i]:
            result.append(arr2[j])
        else:
            result.append(arr1[i])
    stdout.write(' '.join(result) +'\n')
