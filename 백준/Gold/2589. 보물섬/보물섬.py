import sys
from  collections import deque
from itertools import combinations
import copy
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
candi = []
for i in range(N):
    for j in range(M):
        if data[i][j] == 'L':
            candi.append((i,j))

def bfs(one, data):
    visited = [[-1]*M for _ in range(N)]
    dx, dy = [0, 0, 1, -1], [1, -1 , 0, 0]
    dq = deque()
    dq.append(one)
    visited[one[0]][one[1]] = 0
    while dq:
        x, y = dq.popleft()
        prev = visited[x][y]
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0 <= X < N and 0 <= Y < M:
                if visited[X][Y] == -1 and data[X][Y] == 'L':
                    visited[X][Y] = prev + 1
                    dq.append((X,Y))
    maxx = -1
    for i in visited:
        ref = max(i)
        if maxx < ref:
            maxx = ref
    return maxx

maxi = -1
for land in candi:
    route = bfs(land, data)
    if maxi < route:
        maxi = route
print(maxi)