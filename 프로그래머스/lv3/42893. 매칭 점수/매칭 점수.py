import re
from collections import defaultdict
def solution(word, pages):
    answer = [0] * len(pages)
    ind_dict = defaultdict()
    page_dict = defaultdict(list)
    page_pattern = re.compile('<meta property="og:url" content="https://\S*"/>')
    link_pattern = re.compile('<a href="https://\S*">')
    https_pattern = re.compile('https://\S*"')
    word_pattern = re.compile('[a-z]+')
    
    for i in range(len(pages)):
        page = pages[i].lower()
        # 해당 페이지의 주소
        link = page_pattern.findall(page)[0]
        link = https_pattern.findall(link)[0][:-1]
        # 주소 - 인덱스 딕셔너리
        ind_dict[link] = i
        # 단어 등장 횟수
        cnt = 0
        for w in word_pattern.findall(page):
            if w == word.lower():
                cnt += 1
        # 기본 점수 저장
        page_dict[i].extend([cnt, [], 0])
    for i in range(len(pages)):
        page = pages[i].lower()
        # 해당 페이지와 연결된 링크
        ref = link_pattern.findall(page)
        href = [https_pattern.findall(l)[0][:-1] for l in ref]
        # 만약 그 링크가 관심있는 페이지의 링크이면 인덱스 가져옴, 관심 없는거면 -1
        ref = [ind_dict[r] if r in ind_dict else -1 for r in href]
        page_dict[i][-1] = len(ref)
        for j in ref:
            if j != -1:
                page_dict[j][1].append(i)
    for i in range(len(pages)):
        # 현재 페이지로 링크하는 페이지들
        link_from = page_dict[i][1]
        score = 0
        # 링크 점수 계산
        for j in link_from:
            if (page_dict[j][-1])!=0:
                score += (page_dict[j][0] / page_dict[j][-1])
        answer[i] = page_dict[i][0] + score
    maxi = max(answer)
    ind = answer.index(maxi)
        
    return ind