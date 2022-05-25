import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ans = 0
nums = ["1", "2", "3"]
def check(_list, leng):
    last = leng - 1
    half = leng // 2
    rp = False
    for i in range(half):
        if _list[last-i:] == _list[last-i*2-1:last-i]:
            rp = True
            break
    return rp

def dfs(_list):
    global ans
    if len(_list) >= 1:
        repeat = check(_list, len(_list))
        if repeat:
            return
    if len(_list) == N:
        ans = int(''.join(_list))
        return
    for n in nums:
        _list.append(n)
        dfs(_list)
        if len(_list) == N and not check(_list, len(_list)):
            return
        _list.pop()
alist = []
dfs(alist)
print(ans)