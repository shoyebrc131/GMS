from sys import stdin

directions = ('N', 'E', 'S', 'W')
dx, dy = map(int, stdin.readline()[:-1].split())
maze = list()
for i in range(dx):
    maze.append([0 if z == '*' else 1 for z in stdin.readline()[:-1]])
x, y = map(int, stdin.readline()[:-1].split())
x, y = x - 1, y - 1
dir = 0
while True:
    command = stdin.read(1)
    if command == 'R':
        dir = (dir + 1) % 4
    elif command == 'L':
        dir = (dir - 1) % 4
    elif command == 'F':
        if dir == 0:
            if maze[x - 1][y]:
                x -= 1
        elif dir == 1:
            if maze[x][y + 1]:
                y += 1
        elif dir == 2:
            if maze[x + 1][y]:
                x += 1
        elif dir == 3:
            if maze[x][y - 1]:
                y -= 1
    elif command == 'Q':
        break
print(x + 1, y + 1, directions[dir])
