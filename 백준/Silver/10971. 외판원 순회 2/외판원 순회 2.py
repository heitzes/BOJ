import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()
# permutation 쓰는 방법과 dfs 쓰는 방법 두가지 존재

# permutation 풀이
N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
select = [i for i in range(N)]
mini = 100000000

# list(permutations(select, N)) 사용하면 메모리 부족 뜸 !!!! 리스트가 메모리를 많이 잡아먹는듯
for i in permutations(select, N):
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

# dfs 풀이
N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
ans = []
_list = []
def dfs(cnt, _list):
    if len(_list) >= 2:
        if city[_list[-2]][_list[-1]] == 0:
            return
        else:
            cnt += city[_list[-2]][_list[-1]]
    if len(_list) == N:
        if city[_list[-1]][_list[0]] == 0:
            return
        else:
            cnt += city[_list[-1]][_list[0]]
            ans.append(cnt)
            cnt = 0
            return cnt
    for i in range(N):
        if i not in _list:
            _list.append(i)
            dfs(cnt, _list)
            _list.pop()
dfs(0, _list)
print(min(ans))
