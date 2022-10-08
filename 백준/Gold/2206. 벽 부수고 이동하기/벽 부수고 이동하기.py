import sys
from  collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
box = [list(input()) for _ in range(N)]
## 벽 안부쉈을때, 벽 부쉈을때
visited = [[[-1, -1] for i in range(M)] for i in range(N)]
dq = deque()
# x, y, 부숨여부
dq.append([0, 0, 0])
visited[0][0][0] = 1
visited[0][0][1] = 1
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
def bfs():
    while dq: 
        x, y, flag = dq.popleft()
        prev = visited[x][y][flag]
        for i in range(4):
            X, Y = x+dx[i], y+dy[i]
            ## 범위 내에서 방문한적 없을때
            if 0<=X<N and 0<=Y<M and visited[X][Y][flag] == -1:
                ## 만약 벽이라면
                if box[X][Y] == '1':
                    ## 부순적이 없을때
                    if flag == 0:
                        visited[X][Y][1] = prev + 1
                        dq.append([X, Y, 1])
                ## 만약 벽이 아니라면
                else:
                    visited[X][Y][flag] = prev + 1
                    dq.append([X, Y, flag])
    if visited[N-1][M-1][0] != -1 and visited[N-1][M-1][1] != -1:
        return min(visited[N-1][M-1][0], visited[N-1][M-1][1])
    else:
        return max(visited[N-1][M-1][0], visited[N-1][M-1][1])
print(bfs())