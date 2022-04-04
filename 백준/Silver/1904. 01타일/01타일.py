import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
memo = [0] * (1000001)
memo[0] = 0
memo[1] = 1
memo[2] = 2

mod = 15746
if n>=3:
    for i in range(3, n+1):  
        memo[i] = (memo[i-1] % mod) + (memo[i-2] % mod)
print(memo[n] % mod)