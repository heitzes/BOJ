from collections import deque
def solution(distance, rocks, n):
    answer = 0
    rocks = deque(sorted(rocks))
    rocks.appendleft(0)
    rocks.append(distance)
    left, right = 0, distance
    while left < right:
        mid = (left + right) // 2
        if func(rocks, n, mid) < mid:
            right = mid
        else:
            left = mid + 1
            answer = mid
    return answer

def func(rocks, n, dist):
    cnt = 0
    i = 0
    ref = 0
    mini = 1000000000
    while cnt <= n and i < len(rocks)-1:
        cur = rocks[i+1] - rocks[i] + ref
        if cur >= dist:
            ref = 0
            mini = min(mini, cur)
        else:
            cnt += 1
            ref += rocks[i+1] - rocks[i]
        i += 1
    if cnt <= n and i == len(rocks)-1:
        return mini
    else:
        return 0