def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    ## 헤맨부분
    stones.append(right)
    slen = len(stones)
    if k == 1:
        return min(stones)
    while left <= right:
        mid = (left + right) // 2
        #print("left: {} right: {} mid: {}".format(left, right, mid))
        cur_i = -1
        maxi = 0
        for i in range(slen):
            if stones[i] >= mid:
                #print("ind: {} cur_i: {}".format(i, cur_i))
                maxi = i-cur_i
                #print("maxi: ", maxi)
                cur_i = i
            ## 헤맨부분
            if maxi > k:
                break
        #print("maxi: ", maxi)
        if maxi > k:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer