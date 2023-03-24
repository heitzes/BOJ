def solution(new_id):
    answer = ''
    
    # 가능한 문자들
    chr_available = [chr(i) for i in range(97, 123)]
    chr_available.extend(['-', '_', '.'])
    chr_available.extend([str(i) for i in range(10)])

    # 1단계 - 소문자
    new_id = new_id.lower()
    
    # 2단계 - 문자 제거
    new_id = ''.join([i for i in new_id if i in chr_available])
    
    # 3,4단계 - 연속 마침표 제거
    new_id = new_id.split('.')
    new_id = '.'.join([i for i in new_id if i != ''])

    # 5단계
    if not len(new_id):
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.strip('.')

    # 7단계
    if len(new_id) <= 2:
        new_id += (new_id[-1]) * (3-len(new_id))
    
    return new_id