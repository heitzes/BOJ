import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()
n, m, b = map(int, input().split())
maps = []
for _ in range(n):
    maps.extend(list(map(int, input().split())))
mini = min(maps)
maxi = max(maps)
counter = Counter(maps)
best_ans, best_h = float('inf'), maxi
for h in range(maxi, mini-1, -1):
    ans = 0
    cnt = b
    for v, c in counter.items():
        if v > h:
            cnt += c * (v - h)
            ans += c * 2 * (v - h)
        else:
            cnt -= c * (h - v)
            ans += c * (h - v)
    if ans < best_ans and cnt >= 0:
        best_ans = ans
        best_h = h
print(best_ans, best_h)