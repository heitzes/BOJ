import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
namedict = defaultdict(list)
for i in range(N):
    age, name = input().split()
    namedict[int(age)].append(name)

for a in sorted(namedict.keys()):
    for n in namedict[a]:
        print(a, n)