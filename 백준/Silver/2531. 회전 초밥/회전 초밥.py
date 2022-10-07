import sys
def input():
    return sys.stdin.readline().rstrip()
n, d, k, c = map(int, input().split())
nlist = [int(input()) for _ in range(n)]
nlist.extend(nlist[:k-1])
ans = 0
for i in range(n):
    belt = set(nlist[i:i+k])
    if c not in belt:
        belt.add(c)
    ans = max(ans, len(set(belt)))
print(ans)