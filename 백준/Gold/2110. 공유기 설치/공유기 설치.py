import sys
import  bisect
from itertools import combinations, permutations, combinations_with_replacement

def input():
    return sys.stdin.readline().rstrip()

N, C = list(map(int, input().split()))
nlist = []
for _ in range(N):
    nlist.append(int(input()))
nlist = sorted(nlist)

def okay(target):
    res = 1
    piv = nlist[0]
    _list = []
    for i in nlist[1:]:
        bet = i-piv
        if bet >= target:
            _list.append(i)
            res+=1
            piv = i
            if res == C:
                break
        else:
            pass
    return res

left = 0
right = nlist[-1]

while left <= right:
    mid = (left + right) // 2
    res = okay(mid)
    ## 안됨
    if res < C:
        right = mid-1
    else:
        left = mid + 1
        ans = mid
print(ans)