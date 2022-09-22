from collections import defaultdict
def solution(survey, choices):
    score = [0, 3, 2, 1, 0, 1, 2, 3, 0]
    save = defaultdict(int)
    answer = ''
    for i in range(len(survey)):
        s, c = survey[i], choices[i]
        if c > 4:
            save[s[1]] += score[c]
        else:
            save[s[0]] += score[c]
    if save['R'] >= save['T']:
        answer += 'R'
    else:
        answer += 'T'
    if save['C'] >= save['F']:
        answer += 'C'
    else:
        answer += 'F'
    if save['J'] >= save['M']:
        answer += 'J'
    else:
        answer += 'M'
    if save['A'] >= save['N']:
        answer += 'A'
    else:
         answer += 'N'
    return answer