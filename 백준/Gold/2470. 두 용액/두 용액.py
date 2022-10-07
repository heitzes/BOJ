import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
nlist = sorted(list(map(int, input().split())))
ans = float('inf')
start, end = 0, n-1
ans_start, ans_end = 0, n-1
while start < end:
    pre = nlist[start] + nlist[end]
    if abs(ans) > abs(pre):
        ans = pre
        ans_start = start
        ans_end = end
    if pre > 0:
        end -= 1
    elif pre < 0:
        start += 1
    else:
        ans_start = start
        ans_end = end
        break
print(nlist[ans_start], nlist[ans_end])