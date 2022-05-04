import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
coins.sort()
dp = [0] * (K+1)
dp[0] = 1
for coin in coins:
    for i in range(coin, K+1):
        dp[i] += dp[i-coin]
print(dp[K])