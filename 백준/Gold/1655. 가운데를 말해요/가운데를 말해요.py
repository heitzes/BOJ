import heapq
import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())
heapmax, heapmin = [], []
for i in range(N):
    n = int(input())
    if i == 0:
        base = n
        heapq.heappush(heapmax, -n)
    else:
        if n > base:
            heapq.heappush(heapmin, n)
        else:
            heapq.heappush(heapmax, -n)
        if len(heapmin) + 1 < len(heapmax):
            k = heapq.heappop(heapmax)
            heapq.heappush(heapmin, -k)
            base = -heapmax[0]
        elif len(heapmin) > len(heapmax):
            k = heapq.heappop(heapmin)
            heapq.heappush(heapmax, -k)
            base = -heapmax[0]
    print(base)