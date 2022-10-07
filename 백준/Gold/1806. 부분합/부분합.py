from bisect import bisect_left
import sys
def input():
    return sys.stdin.readline().rstrip()
n, m = map(int, input().split())
nlist = list(map(int, input().split()))
sums = [0]
for i in range(n):
    sums.append(sums[-1]+nlist[i])
start = 0
end = bisect_left(sums, m)
initial = end
ans = end
while start < end and end <= n:
    cur = sums[end] - sums[start]
    if end-start < ans and cur >= m:
        ans = end - start 
    if cur > m:
        start += 1
    else:
        end += 1
if ans == len(sums):
    print(0)
else:
    print(ans)