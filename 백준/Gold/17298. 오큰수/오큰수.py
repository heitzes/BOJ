N = int(input())
nlist = list(map(int, input().split()))
stack = [(nlist[0], 0)]
answer = [-1] * (N)
for i in range(1, N):
    if nlist[i] < stack[-1][0]:
        stack.append((nlist[i], i))
    else:
        while stack and stack[-1][0] < nlist[i]:
            popup, ind = stack.pop()
            answer[ind] = nlist[i]
        stack.append((nlist[i], i))
print(*answer)
