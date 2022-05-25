import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
# 숫자는 10개이므로 감소하는 수는 갯수가 정해져있다. 그중 가장 큰 감소하는 수는 9876543210(=ref)
ref = '9876543210'
ans = []
if N >= 1023:
    print(-1)
else:
    for i in range(1,11):
        # ref에 조합을 사용하여 자릿수 별 감소하는 수를 구한다
        # 예를들어 2자리 수의 감소하는 수는 ref에서 숫자 2개를 조합한것(=98, 97 ... etc.)
        # 가장 큰 감소하는 수의 경우 ref에서 숫자 10개를 조합한 것이고 이게 끝이므로 10C1 + 10C2 + ... 10C10 = 2^10 -1 총 1023개가 끝임
        nlist = sorted([int(''.join(i)) for i in (map(list, combinations(ref, i)))])
        ans.extend(nlist)
    print(ans[N])
