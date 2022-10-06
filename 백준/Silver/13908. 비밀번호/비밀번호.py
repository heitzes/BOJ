import sys
from itertools import combinations, permutations, combinations_with_replacement


def input():
    return sys.stdin.readline().rstrip()

n, m = list(map(int, input().split()))
nlist = list(map(int, input().split()))
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = 0
selected = list(combinations_with_replacement(number,n-m))
for i in selected:
    nums = nlist.copy()
    nums.extend(i)
    ans += len(set(permutations(nums, n)))
print(ans)