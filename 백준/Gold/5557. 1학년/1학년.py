import sys, copy
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nlist = list(map(int, input().split()))
target = nlist.pop()
dp = defaultdict(int)
dp[nlist[0]] = 1
for i in range(1, N-1):
    num = nlist[i]
    tmp = copy.deepcopy(dp)
    newdp = defaultdict(int)
    for w, v in tmp.items():
        if num == 0:
            newdp[w] += v*2
        else:
            if w+num <= 20:
                newdp[w+num] += v
            if w-num >= 0:
                newdp[w-num] += v
    dp = newdp
print(dp[target])
