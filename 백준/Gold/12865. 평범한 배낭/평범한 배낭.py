import sys
def input():
    return sys.stdin.readline().rstrip()
    
N, K = map(int, input().split())
dp = {}
dp[0] = 0
for _ in range(N):
    w, v = map(int, input().split())
    ref = dp.copy()
    for tw, tv in ref.items():
        if w+tw <= K:
            if w+tw not in dp:
                dp[w+tw] = v+tv
            else:
                prev = dp[w+tw]
                curr = tv + v
                dp[w+tw] = max(prev, curr)
print(max(dp.values()))