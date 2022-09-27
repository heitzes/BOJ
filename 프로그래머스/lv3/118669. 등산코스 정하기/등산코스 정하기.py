from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    childs = defaultdict(list)
    for a, b, c in paths:
        ## 헤맸던 부분
        ## inten, child를 구분하여 너무 많은 자료구조를 만듬 -> 시간초과
        ## child 안에 intensity까지 한번에 저장
        childs[a].append([b,c])
        childs[b].append([a,c])
    summits, gates = set(summits), set(gates)
    ans = [10000001] * (n+1)
    ## 헤맸던 부분 
    ## 1. gates와 summits에 대한 이중 for문을 돌렸음 
    ## 2. summits에 대해 먼저 for문을 돌렸음
    for gate in gates:
        ans = dijkstra(ans, n, childs, gate, summits, gates)
    answer = []
    maxi = ans[0]
    summits = sorted(summits, reverse=True)
    for summ in summits:
        answer.append([summ, ans[summ]])
    answer = sorted(answer, key = lambda x: (x[-1], x[0]))
    return answer[0]

def dijkstra(ans, n, link, node, summits, gates):
    ans[node] = 0
    hq = []
    ## 헤맸던 부분
    ## heapq 대신 deque를 쓰고 deque를 정렬한 다음 popleft를 하는 방식으로 우선순위를 정했는데
    ## heapq를 사용하면 알아서 정렬되기 때문에 시간복잡도가 더 작음
    heapq.heappush(hq, [0, node])
    while hq:
        _, x = heapq.heappop(hq)
        if x in summits:
            break
        for ch, i in link[x]:
            if ch not in gates:
                cost = max(ans[x], i)
                ## 헤맸던 부분
                ## 다른 노드 거쳐서 가는게 더 짧을때만 heapq에 push해야 함!
                if cost < ans[ch]:
                    ans[ch] = cost
                    heapq.heappush(hq, [ans[ch], ch])
    return ans
