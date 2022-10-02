import sys
import  bisect

def input():
    return sys.stdin.readline().rstrip()

K, N = list(map(int, input().split()))
nlist = []
for _ in range(K):
    nlist.append(int(input()))

def many(_list, leng):
    ans = 0
    for i in _list:
        ans += i//leng
    return ans

def find():
    ans = 0
    left = 1
    right = max(nlist)
    while left <= right:
        mid = (left+right)//2
        ## 불가능한 경우 (랜선이 너무 김)
        if many(nlist, mid) < N :
            right = mid - 1
        ## 가능한 경우 (랜선이 충분히 짧음)
        else:
            left = mid + 1
            ans = mid
    return ans
print(find())