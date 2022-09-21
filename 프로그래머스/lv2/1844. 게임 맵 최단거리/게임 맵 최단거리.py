from collections import deque
def solution(maps):
    answer = bfs(maps)
    return answer

def bfs(game):
    n, m = len(game)-1, len(game[0])-1
    dq = deque([[0, 0, 1]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    find = False
    while dq:
        x, y, r  = dq.popleft()
        if x == n and y == m:
            return r
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a <= n and 0 <= b <= m and game[a][b] == 1:
                game[a][b] += 1
                dq.append([a, b, r + 1])
            # if a == n and b == m:
            #     find = True
            #     return r + 1
            # if a <= n and a >= 0 and b <= m and b >= 0:
            #     if not v[a][b] and game[a][b] == 1:
            #         if [a, b, r + 1] not in dq:
            #             dq.append([a, b, r + 1])
    else:
        return -1            