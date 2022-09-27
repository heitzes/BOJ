from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    answer = []
    childs = defaultdict(list)
    for a, b, c in paths:
        childs[a].append([b,c])
        childs[b].append([a,c])
    summits, gates = set(summits), set(gates)
    ans = [10000001] * (n+1)
    for gate in gates:
        ans = dijkstra(ans, n, childs, gate, summits, gates)
    answer = []
    maxi = ans[0]
    summits = sorted(summits, reverse=True)
    for summ in summits:
        if ans[summ] <= maxi:
            answer = [summ, ans[summ]]
            maxi = ans[summ]
    return answer

def dijkstra(ans, n, link, node, summits, gates):
    ans[node] = 0
    hq = []
    heapq.heappush(hq, [0, node])
    cnt = 0
    while hq:
        cnt += 1
        val, x = heapq.heappop(hq)
        if x in summits:
            continue
        if ans[x] < val:
            continue
        for ch,i in link[x]:
            if ch not in gates:
                cost = max(ans[x], i)
                if cost < ans[ch]:
                    ans[ch] = cost
                    heapq.heappush(hq, [ans[ch], ch])
    return ans
            