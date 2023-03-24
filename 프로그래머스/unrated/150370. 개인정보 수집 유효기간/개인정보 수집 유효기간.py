from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    tdict = defaultdict()
    year, month, day = map(int, today.split('.'))
    calculate = (year-1)*12*28 + (month-1)*28 + day
    
    # 약관 타입, 개월 수로 이루어진 사전
    for term in terms:
        t, month = term.split()
        tdict[t] = int(month)
        
    for i, privacy in enumerate(privacies):
        print(i+1)
        date, t = privacy.split()
        y, m, d = map(int, date.split('.'))
        cal = (y-1)*12*28 + (m-1)*28 + d
        # 유효기간이 지났는지 확인 (사라져야 하는 날이 현재 시점 이하면 삭제)
        if (cal+tdict[t]*28 <= calculate):
            answer.append(i+1)
             
    return answer