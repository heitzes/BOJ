def solution(N, number):
    dp = [set() for _ in range(10)]
    dp[1].add(N)
    for i in range(2, 9):
        for j in range(1, i//2+1):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a*b)
                    dp[i].add(abs(a-b))
                    if b!=0: dp[i].add(a//b)
                    if a!=0: dp[i].add(b//a)
                    dp[i].add(int(str(N)*(i)))
                    
    for i in range(1,9):
        s = dp[i]
        if number in s:
            return i
    return -1