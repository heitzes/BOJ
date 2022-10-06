## 아이디어
# N은 1 이상 9 이하
# number는 1 이상 32,000 이하 -> number에 대해선 O(N^2)로 해결할 수 없다
# dp를 number에 대해 수행하지 않고 사용한 N의 개수에 대해 수행
# ex. N=5, number=12일때
# 5를 1번 사용해서 만들 수 있는 수는 dp[1]
# 5를 2번 사용해서 만들 수 있는 수는 dp[2] = (dp[1], dp[1])에 대해 합,곱,차,나,중복(55)
# 5를 3번 사용해서 만들 수 있는 수는 dp[3] = (dp[1], dp[2])에 대해 합,곱,차,나,중복(555)
# 5를 4번 사용해서 만들 수 있는 수는 dp[4] = (dp[1], dp[3])에 대해 합,곱,차,나,중복(5555) + (dp[2], dp[2])에 대해 합,곱,차,나,중복(5555)
# ...
# 이때 set를 사용하여 중복을 제거하고 number가 dp에 들어있는지 확인할 때 걸리는 시간을 줄인다


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
