import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
relation = [[] for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

ans = 0
def dfs(node, vs):
    global ans
    vs.append(node)
    if len(vs) == 5:
        ans = 1
        return ans
    for ch in relation[node]:
        if ch not in vs:
            dfs(ch, vs)
            vs.pop()
    return ans

for i in range(1, N+1):
    if dfs(i, []) == 1:
        print(1)
        break
else:
    print(0)