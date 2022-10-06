def solution(s):
    answer = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                answer.add(j+1-i)

    return max(answer)