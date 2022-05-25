import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
select = [i for i in range(N)]
#perm = list(permutations(select, N))
#print(len(perm))
mini = 100000000
for i in (permutations(select, N)):
    test1 = list(i)
    test2 = test1[1:] + [test1[0]]
    cnt = 0
    for i,j in zip(test1, test2):
        if city[i][j] == 0:
            break
        else:
            cnt += city[i][j]
    else:
        mini = min(mini, cnt)
print(mini)