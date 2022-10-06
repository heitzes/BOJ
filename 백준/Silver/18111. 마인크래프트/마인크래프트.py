import sys
def input():
    return sys.stdin.readline().rstrip()
n, m, b = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
mini = min([min(i) for i in maps])
maxi = max([max(i) for i in maps])
answer = []
for h in range(mini, maxi+1):
    ans = 0
    cnt = b
    for i in range(n):
        for j in range(m):
            diff = maps[i][j] - h
            if diff > 0:
                cnt += diff
                ans += diff * 2
            else:
                cnt -= -diff
                ans += -diff
    if cnt >= 0:
        answer.append([ans, h])
answer = sorted(answer, key = lambda x: (x[0], -x[1]))
print(*answer[0])