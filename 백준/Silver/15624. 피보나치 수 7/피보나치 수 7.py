import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
memo = [0]*(n+1)
if n > 0:
    memo[1] = 1
    
for i in range(2,n+1):
    memo[i] = (memo[i-1]% 1000000007) + (memo[i-2]% 1000000007)
print(memo[n] % 1000000007)