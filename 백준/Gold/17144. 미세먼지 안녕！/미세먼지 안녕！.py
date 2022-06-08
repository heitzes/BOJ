import sys

def input():
    return sys.stdin.readline().rstrip()


r, c, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]
munji, windx, windy, gong = [], [0, r-1], [0, c-1], []
for i in range(r):
    for j in range(c):
        if maps[i][j] > 0:
            munji.append([i, j, maps[i][j]])
        elif maps[i][j] == -1:
            gong.append(i)

def spread(mun, maps):
    sig = [[0]*c for _ in range(r)]
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    newm, windu, windd = [], [], []
    for m in mun:
        x, y, p = m
        cnt = 0
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0 <= X < r and 0 <= Y < c and maps[X][Y] != -1:
                sig[X][Y] += p // 5
                cnt += 1
        sig[x][y] += - (p // 5) * cnt
    for i in range(r):
        for j in range(c):
            maps[i][j] += sig[i][j]
            if maps[i][j] > 0:
                if i not in windx and i not in gong and j not in windy:
                    newm.append([i, j, maps[i][j]])
                else:
                    if i <= gong[0]:    
                        windu.append([i, j, maps[i][j]])
                    else:
                        windd.append([i, j, maps[i][j]])
                    maps[i][j] = 0
    return newm, windu, windd, maps
def cleanup(windu,maps):
    nwindu = []
    for i in windu:
        if i[0] == gong[0]:
            if i[1] == c-1:
                nwindu.append([i[0]-1, i[1], i[2]])
            else:
                nwindu.append([i[0], i[1]+1, i[2]])
        elif i[0] == 0:
            if i[1] == 0:
                nwindu.append([i[0]+1, i[1], i[2]])
            else:
                nwindu.append([i[0], i[1]-1, i[2]])
        elif i[1] == c - 1:
            nwindu.append([i[0]-1, i[1], i[2]])
        elif i[1] == 0:
            if i[0] + 1 != gong[0]:
                nwindu.append([i[0]+1, i[1], i[2]])
    for n in nwindu:
        maps[n[0]][n[1]] = n[2]
    return nwindu, maps
def cleandown(windd, maps):
    nwindd = []
    for i in windd:
        if i[0] == gong[1]:
            if i[1] == c-1:
                nwindd.append([i[0]+1, i[1], i[2]])
            else:
                nwindd.append([i[0], i[1]+1, i[2]])
        elif i[0] == r-1:
            if i[1] == 0:
                nwindd.append([i[0]-1, i[1], i[2]])
            else:
                nwindd.append([i[0], i[1]-1, i[2]])
        elif i[1] == c-1:
            nwindd.append([i[0]+1, i[1], i[2]])
        elif i[1] == 0:
            if i[0] - 1 != gong[1]:
                nwindd.append([i[0]-1, i[1], i[2]])
    for n in nwindd:
        maps[n[0]][n[1]] = n[2]
    return nwindd, maps
ans = 0
for _ in range(t):
    newm, windu, windd, maps = spread(munji, maps)
    nwu, maps = cleanup(windu, maps)
    nwd, maps = cleandown(windd, maps)
    newm.extend(nwu)
    newm.extend(nwd)
    munji = newm
ans = sum([sum(maps[i]) for i in range(r)]) + 2
print(ans)