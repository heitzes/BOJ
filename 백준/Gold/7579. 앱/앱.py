import sys
from bisect import bisect_left
def input():
    return sys.stdin.readline().rstrip()
    
N, M = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))
maxi = sum(cost)
dp = [[0]*(maxi+1) for _ in range(N)]
for i in range(N):
    m, c = mem[i], cost[i]
    for j in range(1, maxi+1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c]+m)
print(bisect_left(dp[-1], M))