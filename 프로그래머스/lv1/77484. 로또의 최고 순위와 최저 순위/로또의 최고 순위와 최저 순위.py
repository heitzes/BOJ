def solution(lottos, win_nums):
    answer = []
    lotto = set(lottos)
    win = set(win_nums)
    high = len(lotto.intersection(win))
    low = (7 - len(lotto.intersection(win)))
    if low > 6:
        low = 6
    happy = win - lotto
    miss = lottos.count(0)
    if len(happy) >= miss:
        high += miss
    else:
        high += len(happy)
    high = (7 - high)
    if high > 6:
        high = 6
        
    return [high, low]