import sys
def input():
    return sys.stdin.readline().rstrip()

s = int(input())

dp = [i for i in range(s+1)]
for i in range(2, s+1):
    for j in range(i+1, s+1):
        if j % i == 0:
            dp[j] = min(dp[j], dp[i]+1+(j//i-1))
        else:        
            dp[j] = min(dp[j], dp[i]+1+(j//i)+((i)*(j//i+1)-j))
print(dp[-1])