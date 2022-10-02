import sys
import  bisect
def input():
    return sys.stdin.readline().rstrip()

N, M = list(map(int, input().split()))
_list = []
for _ in range(N+M):
    _list.append(input())
nset = set(_list[:N])
mset = set(_list[N:])
inter = nset.intersection(mset)
print(len(inter))
print(*sorted(list(inter)))