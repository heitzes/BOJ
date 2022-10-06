def solution(triangle):
    height = len(triangle)
    dp = [[] for _ in range(height)]
    dp[0] = triangle[0]
    for h in range(1, height):
        tri = triangle[h]
        dp[h].append(tri[0]+dp[h-1][0])
        for i in range(1, h):
            dp[h].append(max(tri[i]+dp[h-1][i], tri[i]+dp[h-1][i-1]))
        dp[h].append(tri[-1]+dp[h-1][-1])
    return max(dp[-1])