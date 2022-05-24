import sys
from itertools import product
import  bisect

def input():
    return sys.stdin.readline().rstrip()

def solution():
    target = int(input())
    n = int(input())
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if n != 0:
        nlist = input().split()
        for i in nlist:
            if i in nums:
                nums.remove(i)
    brute = [i for i in range(999901)]
    check = [k for k in brute if set(list(str(k))).issubset(set(nums))]
    maxi = abs(target-100)
    for num in check:
        count = abs(num-target) + len(str(num))
        if count < maxi:
            maxi = count
    return maxi
print(solution())