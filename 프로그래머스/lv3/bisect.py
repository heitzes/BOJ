from collections import defaultdict
from bisect import bisect_right, bisect_left

def update(c, rlist, p, n, mlist):
    realp = bisect_left(mlist, p)
    if c[0] == 'U':        
        tp = realp - int(c[1])
        return mlist[tp], rlist, mlist
    elif c[0] == 'D':
        tp = realp + int(c[1])
        return mlist[tp], rlist, mlist
    elif c[0] == 'C':  
        rlist.append(p)
        if p == mlist[-1]:
            newp = mlist[realp-1]
            mlist = mlist[:realp]
            return newp, rlist, mlist
        else:
            newp = mlist[realp+1]
            mlist = mlist[:realp] + mlist[realp+1:]
            return newp, rlist, mlist
    else:
        realp = bisect_left(mlist, rlist[-1])
        if realp == len(mlist):
            mlist.append(rlist.pop())
        else:
            mlist.insert(realp, rlist.pop())
        return p, rlist, mlist

def solution(n, k, cmd):
    answer = ['O'] * n    
    pos, remove, remain = k, [], [i for i in range(n)]
    for c in cmd:
        sp = c.split()
        pos, remove, remain = update(sp, remove, pos, n, remain)
    for r in remove:
        answer[r] = 'X'
    return ''.join(answer)
