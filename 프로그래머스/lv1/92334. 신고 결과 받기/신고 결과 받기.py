from collections import defaultdict
def solution(id_list, report, k):
    # 1:N 신고, 중복 신고는 1회로 처리
    # K명 이상한테 신고되면 정지, 신고자한테 메일 발송
    # 처리 결과 메일 받은 횟수 구하기 (즉, 내가 정지시킨 사람 수 구하기)
    # 유저, 신고한 사람, 정지여부
    # 정지 -> 유저 테이블에 +1
    answer = []
    reported = defaultdict(set)
    reporter = defaultdict(int)
    for rep in report:
        a, b = rep.split()
        reported[b].add(a)
    for val in reported.values():
        if len(val) >= k:
            for r in val:
                reporter[r] += 1
    for user in id_list:
        answer.append(reporter[user])
    return answer