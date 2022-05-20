import sys
from  collections import deque, defaultdict
import copy
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for i in range(N + 1)]
for i in range(N-1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
target = list(map(int, input().split()))


chtree = [[] for i in range(N+1)]
ptree = [0] * (N+1)

def make_tree(x, graph, visited):
    visited[x] = 1
    for next in graph[x]:
        if not visited[next]:
            make_tree(next, graph, visited)
        else: # 트리 상에서 내 부모다.
            chtree[next].append(x)
            ptree[x] = next

# 1번 노드를 루트로 잡자.
visited = [0] * (N + 1)
make_tree(1, graph, visited)

check = [0] * (N+1)
check[1] = 1
for i, j in zip(target, target[1:]):
    if len(chtree[i]) != 0:
        if ptree[j] == i and check[j] != 1:
            check[j] = 1
            continue
        else:
            print(0)
            break
    else:
        find = False
        p = i
        while p != 1 and not find:
            p = ptree[p]
            if ptree[j] == p:
                find = True
        if find == False:
            print(0)
            break
else:
    print(1)