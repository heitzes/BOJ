import sys, re
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    
# 첫번째 방법 - 정규표현식 사용
s = input()
if s[0] != '-':
    nums = deque(map(int, re.split("[-*/+]", s)))
    ops = deque(re.split("[0-9]+", s)[1:-1])
else:
    nums = deque(map(int, re.split("[-*/+]", s[1:])))
    nums.insert(0, -nums.popleft())
    ops = deque(re.split("[0-9]+", s[1:])[1:-1])

# 두번째 방법 - set, replace 사용
# sets = set(s)
# while '*' in sets or '/' in sets or '+' in sets or '-' in sets:
#     s = s.replace('*', ' a ')
#     s = s.replace('/', ' b ')
#     s = s.replace('+', ' c ')
#     s = s.replace('-', ' d ')
#     sets = set(s)
# slist = s.split() 

# 세번째 방법 - for문으로 replace 사용
# ``이 방법 사용하면 시간초과뜸!
# refs = s[0]
# for i in s[1:]:
#     if i in ['+', '-', '*', '/']:
#         refs += ' {} '.format(i)
#     else:
#         refs += i
# slist = refs.split()``

# odict = {'a': '*', 'b': '/', 'c': '+', 'd': '-'}
pdict = {'*': 1, '/': 1, '+': 0, '-': 0}
# nlist, olist = [], []
# if slist[0] == 'd':
#     slist = slist[1:]
#     slist[0] = str(-int(slist[0]))
# for i in slist:
#     try:
#         nlist.append(int(i))
#     except:
#         olist.append(odict[i])

nlist = nums
olist = ops
def calculate(o, a, b):
    if o == '*':
        return a*b
    elif o == '/':
        return int(a/b)
    elif o == '+':
        return a+b
    else:
        return a-b
while True:
    if len(olist) > 1:
        up, down = pdict[olist[0]], pdict[olist[-1]]
        if up > down:
            oup = olist.popleft()
            a, b = nlist.popleft(), nlist.popleft() 
            calc = calculate(oup, a, b)
            nlist.insert(0, calc)
        elif up < down:
            odown = olist.pop()
            a, b = nlist.pop(), nlist.pop()
            calc = calculate(odown, b, a)
            nlist.append(calc)
        else:
            upc = calculate(olist[0], nlist[0], nlist[1])
            downc = calculate(olist[-1], nlist[-2], nlist[-1])
            if upc >= downc:
                olist.popleft()
                nlist.popleft()
                nlist.popleft()
                nlist.insert(0, upc)
            else:
                olist.pop()
                nlist.pop()
                nlist.pop()
                nlist.append(downc)
    elif len(olist) == 1:
        print(calculate(olist.pop(), nlist[0], nlist[1]))
        break
    else:
        print(nlist[0])
        break
