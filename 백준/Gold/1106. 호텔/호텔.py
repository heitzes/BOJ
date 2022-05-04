import sys

def input():
    return sys.stdin.readline().rstrip()

C, N = map(int, input().split())
dp = [1e9] * (1001)
for i in range(N):
    pay, peop = map(int, input().split())
    for j in range(1001):
        if j <= peop:
            dp[j] = min(dp[j], pay)
        else:
            dp[j] = min(min(dp[j-peop:j])+pay, min(dp[j:]))
print(min(dp[C:]))