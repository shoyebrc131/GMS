from math import sqrt
repeat = int(input())
for i in range(repeat):
    coord1 = input().split()
    x1, y1 = float(coord1[0]), float(coord1[1])
    rad = float(input())
    coord2 = input().split()
    x2, y2 = float(coord2[0]), float(coord2[1])
    dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if dist > rad:
        print("The point is not inside the circle")
    else:
        print("The point is inside the circle")
