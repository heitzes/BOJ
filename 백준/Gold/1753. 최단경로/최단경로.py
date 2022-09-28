import sys
from collections import defaultdict
import heapq

V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
paths = defaultdict(list)
for _ in range(E):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    paths[u].append([w,v])
ans = [float('INF')]*(V+1)
ans[k] = 0
hq = []
heapq.heappush(hq, [0, k])
while hq:
    val, x = heapq.heappop(hq)
    if ans[x] < val:
        continue
    for i, ch in paths[x]:
        cost = val + i
        if cost < ans[ch]:
            ans[ch] = cost
            heapq.heappush(hq, [ans[ch], ch])
for i in range(1,V+1):
    if ans[i] != float('inf'):
        print(ans[i])
    else:
        print('INF')
