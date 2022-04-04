import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
numlist = [int(input()) for _ in range(n)]
memo = [0] * 11
memo[1] = 1
memo[2] = 2
memo[3] = 4
memo[4] = 7
for i in range(5, 11):
    memo[i] = memo[i-3] + memo[i-2] + memo[i-1]

for n in numlist:
    print(memo[n])