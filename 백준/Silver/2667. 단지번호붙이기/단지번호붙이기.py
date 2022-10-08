n = int(input())
homes = [[] for _ in range(n)]
for i in range(n):
    homes[i] = list(map(int, input()))
visited = [[False]*(n+1) for i in range(n)]

def is_terminal(a,b):
    if a == 0 or b == 0 or a == n-1 or b == n-1:
        return True
    else:
        return False

def direction(a,b):
    if not is_terminal(a,b):
        actions = [[0,1], [0,-1], [1,0], [-1,0]]
    else:
        if a == 0 and b == 0:
            actions = [[0,1], [1,0]]
        elif a == 0 and b == n-1:
            actions = [[0,-1],[1,0]]
        elif a == n-1 and b == 0:
            actions = [[-1,0],[0,1]]
        elif a == n-1 and b == n-1:
            actions = [[-1,0],[0,-1]]
        elif a == 0:
            actions = [[0,1], [0,-1], [1,0]]
        elif a == n-1:
            actions = [[0,1], [0,-1], [-1,0]]
        elif b == 0:
            actions = [[0,1], [1,0], [-1,0]]
        elif b == n-1:
            actions = [[0,-1], [1,0], [-1,0]]
    return actions

def dfs(r,c,visited):
    global pep
    pep += 1
    visited[r][c] = True
    actions = direction(r,c)
    for act in actions:
        new_r, new_c = r+act[0], c+act[1]
        if homes[new_r][new_c] == 1 and visited[new_r][new_c] == False:
            dfs(new_r, new_c, visited)
            
cnt = 0
people = []
for i in range(n):
    for j in range(n):
        if homes[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            pep = 0
            dfs(i,j,visited)
            people.append(pep)

print(cnt)
for p in sorted(people):
    print(p)