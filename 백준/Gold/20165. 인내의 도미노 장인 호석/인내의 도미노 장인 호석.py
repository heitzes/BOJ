import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cmds, recover = [], []
for i in range(r):
    x, y, z = input().split()
    xx, yy = map(int, input().split())
    cmds.append((int(x)-1, int(y)-1, z))
    recover.append((xx-1, yy-1, maps[xx-1][yy-1]))

def domino(maps, c, n, m):
    visited, q = [], deque()
    if c[-1] == 'E':
        q.append(c[1])
        while q:
            pos = q.popleft()
            if pos not in visited:
                visited.append(pos)
            for i in range(pos, pos+maps[c[0]][pos]):
                if i not in visited and i < m and maps[c[0]][i] != 'F':
                    q.append(i)
        for j in visited:
            maps[c[0]][j] = 'F'
    if c[-1] == 'W':
        q.append(c[1])
        while q:
            pos = q.popleft()
            if pos not in visited:
                visited.append(pos)
            for i in range(pos, pos-maps[c[0]][pos], -1):
                if i not in visited and i >= 0 and maps[c[0]][i] != 'F':
                    q.append(i)
        for j in visited:
            maps[c[0]][j] = 'F'
    if c[-1] == 'S':
        q.append(c[0])
        while q:
            pos = q.popleft()
            if pos not in visited:
                visited.append(pos)
            for i in range(pos, pos+maps[pos][c[1]]):
                if i not in visited and i < n and maps[i][c[1]] != 'F':
                    q.append(i)
        for j in visited:
            maps[j][c[1]] = 'F'
    if c[-1] == 'N':
        q.append(c[0])
        while q:
            pos = q.popleft()
            if pos not in visited:
                visited.append(pos)
            for i in range(pos, pos-maps[pos][c[1]], -1):
                if i not in visited and i >= 0 and maps[i][c[1]] != 'F':
                    q.append(i)
        for j in visited:
            maps[j][c[1]] = 'F'
    return len(visited)

ans = 0 
for i in range(r):
    cmd, rcv = cmds[i], recover[i]
    ans += domino(maps, cmd, n, m)
    maps[rcv[0]][rcv[1]] = rcv[2]

for i in range(n):
    for j in range(m):
        if maps[i][j] != 'F':
            maps[i][j] = 'S'
print(ans)
for a in [' '.join(i) for i in maps]:
    print(a)