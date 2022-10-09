import heapq
def solution(routes):
    answer = 0
    hq = []
    for route in routes:
        heapq.heappush(hq, [route[1], route[0]])
    while hq:
        key = heapq.heappop(hq)
        answer += 1
        while hq and (hq[0][1] <= key[0]):
            heapq.heappop(hq)
    return answer