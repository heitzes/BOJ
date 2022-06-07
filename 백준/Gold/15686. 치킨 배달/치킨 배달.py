import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def compare(clist, p):
    mini = 100000000
    for c in clist:
        mini = min(mini, abs(c[0]-p[0])+abs(c[1]-p[1]))
    return mini

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(n)]
house, chicken = [], []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken.append((i, j))
        elif maps[i][j] == 1:
            house.append((i, j))

ans = 10000000000
for ch in combinations(chicken, m):
    cnt = 0
    for h in house:
        cnt += compare(list(ch), h)
    ans = min(cnt, ans)
print(ans)