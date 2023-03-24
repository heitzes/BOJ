from collections import defaultdict
def solution(survey, choices):
    answer = ''
    # 왼쪽에 있는게 비동의, 오른쪽에 있는게 동의 점수
    # 중앙값 4와 비교해서 점수 부여 (4보다 작으면 왼쪽, 4보다 크면 오른쪽)
    # 'AN'에 선택 5 -> 1점을 N에 부여
    # 동일 점수라면 사전순으로
    one = {'R':0, 'T':0}
    two = {'C':0, 'F':0}
    three = {'J':0, 'M':0}
    four = {'A':0, 'N':0}
    find = {'R': 0, 'T':0, 'C':1, 'F':1, 'J':2, 'M':2, 'A':3, 'N':3}
    test = [one, two, three, four]
    
    for s, ch in zip(survey, choices):
        point = test[find[s[0]]]
        if ch > 4:
            point[s[1]] += ch - 4
        else:
            point[s[0]] += 4 - ch
    
    for t in test:
        result = sorted(t.items(), key = lambda x: -x[-1])
        answer += result[0][0]
        
    return answer
    