# 징검다리 건너기

def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    ## 헤맨부분
    # 맨 마지막 돌에서 개울의 오른쪽 건너편으로 이동할때의 점프길이도 확인해야됨
    stones.append(right)
    slen = len(stones)
    if k == 1:
        return min(stones)
    while left <= right:
        mid = (left + right) // 2
        ## 시작지점인 개울의 왼쪽에 있는 상태의 index를 -1로 지정
        cur_i = -1
        maxi = 0
        for i in range(slen):
            if stones[i] >= mid:
                ## 헤맨부분
                # maxi = max(maxi, i-cur_i) 로 작성했는데, 생각해보니 maxi 값을 얻는게 중요한게 아님
                # i-cur_i가 k보다 큰 경우를 찾는게 목적이므로 매번 max 연산을 하지 않아도 됨. 가장 큰 값을 찾는게 목적이 아니라 큰 값이 있으면 탈출하는게 목적이므로
                maxi = i-cur_i
                cur_i = i
                ## 큰 값을 찾으면 즉시 for 반복문 탈출
                if maxi > k:
                    break
        if maxi > k:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer
