import itertools
import copy
n, m = list(map(int, input().split()))
lab = []
mx = [1,-1,0,0]
my = [0,0,1,-1]  
for _ in range(n):
    lab.append(list(map(int, input().split())))
def search(maps, t):
    nlist = []
    if t == 'virus':
        for i in range(n):
            for j in range(m):
                if lab[i][j] == 2:
                    nlist.append([i,j])
    else:
        for i in range(n):
            for j in range(m):
                if lab[i][j] == 0:
                    nlist.append([i,j])
    return nlist
def dfs(copy, virus):
    while len(virus)!= 0:
        i, j = virus.pop()
        for k in range(4):
            x, y = i + mx[k], j + my[k]
            if x >= 0 and x < n and y >=0 and y < m:
                if copy[x][y] == 0:
                    copy[x][y] = 2
                    virus.append([x, y])
    return copy
maxi = 0
zeros = search(lab, 'zeros')
virus_org = search(lab, 'virus')
for a,b,c in itertools.combinations(zeros,3):
    virus = copy.deepcopy(virus_org)
    copylab = copy.deepcopy(lab)
    copylab[a[0]][a[1]], copylab[b[0]][b[1]], copylab[c[0]][c[1]] = 1, 1, 1
    zero = 0
    for line in dfs(copylab, virus):
        zero += line.count(0)
    if zero >= maxi:
        maxi = zero
print(maxi)