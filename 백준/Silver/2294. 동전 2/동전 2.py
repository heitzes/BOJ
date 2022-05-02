import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
coins.sort()
dp = [int(1e9)] * 10001
dp[0] = 0
for i in range(1, K+1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i-coin] + 1)
        else:
            break
if dp[K] == int(1e9):
    print(-1)
else:
    print(dp[K])