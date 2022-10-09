def solution(routes):
    answer = 1
    routes = sorted(routes, key = lambda x: (x[0], x[1]))
    cur, ref = min(routes[0]), max(routes[0])
    while True:
        route = routes.pop(0)
        start, end = min(route), max(route)
        if cur <= start:
            if start <= ref:
                cur = start
                ref = min(end, ref)
            else:
                answer += 1
                cur = start
                ref = end
        if len(routes) == 0:
            break
        
    return answer