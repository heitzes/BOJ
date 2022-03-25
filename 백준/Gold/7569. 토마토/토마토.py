import sys
from  collections import deque, defaultdict

def input():
    return sys.stdin.readline().rstrip()

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for j in range(N)] for i in range(H)]
visited = [[[-1]*M for j in range(N)] for i in range(H)]
dq = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 1:
                dq.append((h,i,j))
                visited[h][i][j] = 0
dh = [1, -1]
dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]

def bfs():
    while dq:
        z, x, y = dq.popleft()
        prev = visited[z][x][y]
        for i in range(4):
            Z, X, Y = z, x+dx[i], y+dy[i]
            if 0<=X<N and 0<=Y<M and box[Z][X][Y] == 0 and visited[Z][X][Y] == -1:
                dq.append((Z,X,Y))
                visited[Z][X][Y] = prev + 1
                box[Z][X][Y] = 1
        for h in range(2):
            Z, X, Y = z+dh[h], x, y
            if 0<=Z<H and box[Z][X][Y] == 0 and visited[Z][X][Y] == -1:
                dq.append((Z,X,Y))
                visited[Z][X][Y] = prev + 1
                box[Z][X][Y] = 1
    else:
        for h in range(H):
            for i in range(N):
                for j in range(M):
                    if box[h][i][j] == 0:
                        return -1
        else:
            return visited[z][x][y]
print(bfs())