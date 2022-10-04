import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
s = int(input())

# DP 풀이
dp = [i for i in range(s+1)]
for i in range(2, s+1):
    for j in range(i+1, s+1):
        ## j가 i의 배수라면 복사 한번 후 붙여넣기 여러번
        if j % i == 0:
            dp[j] = min(dp[j], dp[i]+1+(j//i-1))
        ## j가 i의 배수가 아니라면 여러번 붙여넣기 한 뒤에 삭제
        else:
            ## 헤맨 부분 ##
            # 삭제해야할 이모티콘 개수 구하는 부분에서 실수했다
            # 손코딩 or 디버깅으로 예시 꼭 확인해볼것!ㅠㅠ
            dp[j] = min(dp[j], dp[i]+1+(j//i)+((i)*(j//i+1)-j))
print(dp[-1])

# BFS 풀이
dq = deque([[1, 0]])
## 헤맨 부분 ##
# vi를 -1로 채워두고 -1이면 방문 안한것 처리
# 방문 여부와 횟수를 한꺼번에 vi로 처리할 수 있음
# bfs와 queue를 사용함으로서 최소거리를 보장한다
vi = [[-1]*(s+1) for _ in range(s+1)]
vi[1][0] = 0
while dq:
    sc, cl = dq.popleft()
    if vi[sc][sc] == -1:
        dq.append([sc, sc])
        vi[sc][sc] = vi[sc][cl] + 1
    if sc+cl <= s and vi[sc+cl][cl] == -1:
        dq.append([sc+cl, cl])
        vi[sc+cl][cl] = vi[sc][cl] + 1
    if sc >= 1 and vi[sc-1][cl] == -1:
        dq.append([sc-1, cl])
        vi[sc-1][cl] =vi[sc][cl] + 1
print(min(vi[-1][1:]))
