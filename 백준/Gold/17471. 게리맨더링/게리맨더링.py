import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

# 2개의 선거구로 나누되 두 선거구 인구수가 최소가 되어야함
# 하나의 선거구 안의 구역들은 서로 연결되어야있어야함 (다른 구역 경유 가능, 단 같은 선거구여야 함)
N = int(input())
peop = [0] + list(map(int, input().split()))
maps = [[] for _ in range(N+1)]
for i in range(1, N+1):
    link = list(map(int, input().split()))
    if link[0] != 0:
        maps[i] = link[1:]
dev = set([i+1 for i in range(N)])
comb = []
for k in range(1, N//2+1):
    ref = [set(i) for i in combinations(dev, k)]
    comb.extend(ref)

def dfs(n, visited, leng, st):
    visited.append(n)
    # 종료조건
    if len(visited) == leng:
        return visited
    for i in maps[n]:
        if i not in visited and i in st:
            dfs(i, visited, leng, st)
    return visited

mini = 10000
summ = sum(peop)
for sect in comb:
    other = list(dev - sect)
    sect = list(sect)
    ds = dfs(sect[0], [], len(sect), sect)
    do = dfs(other[0], [], len(other), other)
    if len(sect) == len(ds) and len(other) == len(do):
        sp = sum([peop[i] for i in sect])
        mini = min(mini, abs(summ - sp*2))
if mini == 10000:
    print(-1)
else:
    print(mini)