from collections import Counter, defaultdict
def solution(gems):
    answer = []
    s, e, pre_e = 0, 0, -1
    shop = set(gems)
    count = defaultdict(int)
    while s <= e and e < len(gems):
        if e != pre_e:
            count[gems[e]] += 1
        pre_e = e
        if len(count) < len(shop):
            e += 1
        elif len(count) == len(shop):
            if count[gems[s]] > 1:
                count[gems[s]] -= 1
                s += 1
            else:
                answer.append([e-s, s+1, e+1])
                e += 1
    # while s <= e and e < len(gems):
    #     count = Counter(gems[s:e+1])
    #     if len(count) < len(shop):
    #         e += 1
    #     elif len(count) == len(shop):
    #         if count[gems[s]] > 1:
    #             s += 1
    #         else:
    #             answer.append([e-s, s+1, e+1])
    #             e += 1
    answer.sort()
    return answer[0][1:]