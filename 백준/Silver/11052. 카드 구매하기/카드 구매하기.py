import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
cards = list(map(int, input().split()))
dp = [0] * 1001
for idx, val in enumerate(cards):
    dp[idx+1] = val

for i in range(2, N+1):
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[N])