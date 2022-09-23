import re
from itertools import combinations, permutations
def solution(user_id, banned_id):
    answer = 0
    blen = len(banned_id)
    comb = list(map(list, combinations(user_id, blen)))
    for c in comb:
        perm = list(map(list, permutations(c, blen)))
        for ids in perm:
            for i in range(blen):
                bid = banned_id[i]
                pattern = re.compile(bid.replace('*', '[a-z0-9]'))
                result = (pattern.match(ids[i]))
                if result == None or len(ids[i]) != len(bid):
                    break
            else:
                answer += 1
                break
    return answer