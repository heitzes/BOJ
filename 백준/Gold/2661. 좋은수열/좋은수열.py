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
    # 제약조건: 중복되는 인접 수열이 있으면 안됨 -> 이전 순열로 돌아감
    if len(_list) >= 1:
        repeat = check(_list, len(_list))
        if repeat:
            return
    # 종료조건: 길이가 N이 되면 종료
    if len(_list) == N:
        ans = int(''.join(_list))
        return
    for n in nums:
        _list.append(n)
        dfs(_list)
        # 길이가 N이 되면 가장 작은 좋은 순열을 찾은 것이므로 더이상 순열을 찾아보지 않아도 됨
        # 만약 check로 중복을 확인하지 않으면 N==2일때 오류생김
        if len(_list) == N and not check(_list, len(_list)):
            return
        # 11 같이 제약조건에 걸리는 순열일 경우 pop해서 이전 순열인 1로 돌아감
        _list.pop()
alist = []
dfs(alist)
print(ans)
