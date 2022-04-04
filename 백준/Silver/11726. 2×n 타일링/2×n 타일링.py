import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
memo = [0] * 1001
memo[1] = 1
memo[2] = 2
memo[3] = 3
memo[4] = 5
mod = 10007
if n>=5:
    for i in range(5,n+1):
        memo[i] = (memo[i-1]%mod) + (memo[i-2]%mod)
print(memo[n]%mod)