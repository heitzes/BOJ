import sys
from  collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
visited = [-1]*200000
dq = deque()
dq.append(N)
visited[N] = 0
found = False
while dq and not found:
    x = dq.popleft()
    prev = visited[x]
    if x == K:
        found = True
        print(prev)
    else:
        if x+1 < 200000 and visited[x+1] == -1:
            dq.append(x+1)
            visited[x+1] = prev+1
        if x-1 >= 0 and visited[x-1] == -1:
            dq.append(x-1)
            visited[x-1] = prev+1
        if x*2 < 200000 and visited[x*2] == -1:
            dq.append(x*2)
            visited[x*2] = prev+1
