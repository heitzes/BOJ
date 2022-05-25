import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ref = '9876543210'
ans = []
if N >= 1023:
    print(-1)
else:
    for i in range(1,11):
        nlist = sorted([int(''.join(i)) for i in (map(list, combinations(ref, i)))])
        ans.extend(nlist)
    print(ans[N])