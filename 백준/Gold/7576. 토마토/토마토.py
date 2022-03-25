import sys
from  collections import deque, defaultdict

def input():
    return sys.stdin.readline().rstrip()

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for i in range(N)]
dq = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            dq.append((i,j))
            visited[i][j] = 0
dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]

def bfs():
    while dq:
        node = dq.popleft()
        x, y = node
        prev = visited[x][y]
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0<=X<N and 0<=Y<M and box[X][Y] == 0 and visited[X][Y] == -1:
                dq.append((X,Y))
                box[X][Y] = 1
                visited[X][Y] = prev + 1
    else:
        for i in range(N):
            for j in range(M):
                if box[i][j] == 0:
                    return -1
        else:
            return visited[x][y]

print(bfs())