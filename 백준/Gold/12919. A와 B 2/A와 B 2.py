import sys

def input():
    return sys.stdin.readline().rstrip()

S = input()
T = input()
check_list = [T]
find = False
while not find:
    if not check_list:
        break
    if len(check_list[0]) == len(S):
        find = True
    else:
        ref = check_list[:]
        for i in check_list:
            check = ref.pop(0)
            if check[0] == 'A' and check[-1] == 'A':
                ref.append(check[:-1])
            elif check[0] == 'B' and check[-1] == 'B':
                ref.append(check[::-1][:-1])
            elif check[0] == 'B' and check[-1] == 'A':
                ref.append(check[:-1])
                ref.append(check[::-1][:-1])
        check_list = ref[:]
if find == True:
    if S in check_list:
        print(1)
    else:
        print(0)
else:
    print(0)