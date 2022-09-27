from collections import deque
def solution(rc, operations):
    answer = []
    newr = deque([])
    newc = deque([deque(), deque()])
    for line in rc:
        newr.append(deque(line[1:-1]))
        newc[0].append(line[0])
        newc[-1].append(line[-1])
    for op in operations:
        if op == 'Rotate':
            newr[-1].append(newc[-1].pop())
            newc[0].append(newr[-1].popleft())
            newr[0].appendleft(newc[0].popleft())
            newc[-1].appendleft(newr[0].pop())
        else:
            newr.appendleft(newr.pop())
            newc[0].appendleft(newc[0].pop())
            newc[-1].appendleft(newc[-1].pop())
    for i in range(len(rc)):
        newr[i].appendleft(newc[0][i])
        newr[i].append(newc[-1][i])
        answer.append(list(newr[i]))
    return answer