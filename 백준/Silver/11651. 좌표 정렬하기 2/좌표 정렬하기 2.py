import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nlist = []
for i in range(N):
    x, y = map(int, input().split())
    nlist.append((x, y))

nlist = sorted(nlist, key = lambda x: (x[1], x[0]))
for n in nlist:
    print(*n)