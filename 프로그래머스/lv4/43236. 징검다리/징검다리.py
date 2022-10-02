from collections import deque
def solution(distance, rocks, n):
    sorted_rocks = sorted(rocks)
    sorted_rocks.append(distance)
    left, right = 0, distance
    while left <= right:
        cur, cnt = 0, 0
        mid = (left + right) // 2
        for i in sorted_rocks:
            if i - cur < mid:
                cnt += 1
            else:
                cur = i
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer