import sys
from collections import defaultdict
# 11
# 100 10 2 1 2 50 10 5 100 7 51
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nlist = list(map(int, input().split()))
answer = [0] * (N)
answer[0] = 1
panswer = []
for i in range(1, N):
    maxi = 0
    for j in range(i):
        if nlist[j] < nlist[i]:
            if answer[j] > maxi:
                maxi = answer[j]
    answer[i] = maxi + 1
ans = max(answer)
pdict = defaultdict(list)

for i in range(N):
    pdict[answer[i]].append(i)

curr, currind = 1001, N
for j in range(ans, 0, -1):
    for ind in pdict[j]:
        if ind < currind and nlist[ind] < curr:
            curr = nlist[ind]
            currind = ind
    panswer.append(curr)
print(ans)
print(*panswer[::-1])