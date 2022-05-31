import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nlist = list(map(int, input().split()))
stack = deque()
stack.append((-1, 1000001))
answer = [-1] * N
for ind, val in enumerate(nlist):    
    while stack[-1][1] < val:
        pind, _ = stack.pop()
        answer[pind] = val
    stack.append((ind, val))
print(*answer)
