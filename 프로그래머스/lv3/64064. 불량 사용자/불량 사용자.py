import re
from itertools import combinations, permutations
def solution(user_id, banned_id):
    answer = 0
    blen = len(banned_id)
    # 유저 조합
    comb = list(map(list, combinations(user_id, blen)))
    for c in comb:
        # 유저 조합으로 만든 유저 순서 (banned_id의 순서에 맞추기 위해)
        # ex. abc123와 frodo를 유저 조합으로 뽑았을 때, 순서가 frodo abc123이 되어야 banned_id에 매칭됨 
        perm = list(map(list, permutations(c, blen)))
        for ids in perm:
            for i in range(blen):
                bid = banned_id[i]
                pattern = re.compile(bid.replace('*', '[a-z0-9]'))
                result = (pattern.match(ids[i]))
                # 하나라도 매칭되지 않으면 바로 break
                if result == None or len(ids[i]) != len(bid):
                    break
            # 모두 매칭이 되었다면 같은 유저 조합 안의 다른 순서는 볼 필요 없으므로 break
            # ex. frodo crodo abc123이 되면 crodo frodo abc123을 굳이 확인해볼 필요가 없음. 이미 성공한 조합이므로
            else:
                answer += 1
                break
    return answer