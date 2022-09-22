from collections import deque
def solution(queue1, queue2):
    ans = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    ref = [sum(queue1), sum(queue2)]
    loop = queue1.copy()
    target = sum(ref) / 2
    same = False
    if int(target) != target:
        return -1
    while True:
        if ans > 600000:
            break
        if ref[0] > ref[1]:
            ref[0] -= queue1[0]
            ref[1] += queue1[0]
            queue2.append(queue1.popleft())
            ans += 1
        elif ref[1] > ref[0]:
            ref[0] += queue2[0]
            ref[1] -= queue2[0]
            queue1.append(queue2.popleft())
            ans += 1
        else:
            same = True
            break
        if queue1 == loop:
            break
    if same:
        return ans
    else:
        return -1