import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nlist = [int(i) for i in input().split()]
nlist.sort()
perm = permutations(nlist, M)
sorted_perm = sorted(list(set(list(perm))))
for i in sorted_perm:
    print(*i)