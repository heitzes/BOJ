import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
nlist = list(map(int, input().split()))
ans = [1] * (n)
maxi = 0
for i in range(1,n):
    if nlist[i] > nlist[maxi]:
        ans[i] = ans[maxi] + 1
        maxi = i
    else:
        maxj = 0
        for k in range(i):
            if nlist[i-1-k] < nlist[i]:
                if ans[i-1-k] > maxj:
                    maxj = ans[i-1-k]
        ans[i] = maxj + 1
        if ans[i] == ans[maxi]:
            if nlist[i] < nlist[maxi]:
                maxi = i
        else:
            if nlist[i] > nlist[maxi]:
                maxi = i
print(max(ans))