length = int(input())
k = []
for i in range(length):
    k.append(int(input()))
l = sorted(k)
if l == k or l[::-1] == k:
    print("YES")
else:
    print("NO")
