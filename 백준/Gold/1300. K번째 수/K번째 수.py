import sys
from bisect import bisect_left
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
k = int(input())
left, right = 0, min(10**9, N**2)
ans = (left + right) // 2
k = k - 1
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for j in range(N):
        cnt += min(N, mid//(j+1))
        if cnt > k:
            break
    if cnt > k:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
print(ans)